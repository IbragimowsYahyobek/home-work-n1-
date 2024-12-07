import asyncio
import random


from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor 


from config import token 

bot = Bot(token=token)
dp = Dispatcher(bot)

start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
start_menu.add(KeyboardButton("Игра"))
start_menu.add(KeyboardButton("Наши новости"))

game_menu = ReplyKeyboardMarkup(resize_keyboard=True)
game_menu.add(KeyboardButton("Камен, ножницы, бумага"))
game_menu.add(KeyboardButton("Рандомайзер"))
game_menu.add(KeyboardButton("Назад"))

rps_menu = ReplyKeyboardMarkup(resize_keyboard=True)
rps_menu.add(KeyboardButton("Камень"))
rps_menu.add(KeyboardButton("Ножницы"))
rps_menu.add(KeyboardButton("Бумага"))
rps_menu.add(KeyboardButton("Назад"))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        """Добро пожаловать!
          Пожалуйста, выберите действие:""",
        reply_markup=start_menu
    )



@dp.message_handler(lambda message: message.text == "Игра")
async def game_menu_display(message: types.Message):
    await message.answer(
        "Выберите, что вы хотите сделать:",
        reply_markup=game_menu
    )

@dp.message_handler(lambda message: message.text == "Камен, ножницы, бумага")
async def rps_menu_display(message: types.Message):
    await message.answer(
        "Выберите один вариант:",
        reply_markup=rps_menu
    )

@dp.message_handler(lambda message: message.text in ["Камень", "Ножницы", "Бумага"])
async def play_rps(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])

    result = "Ничья"
    if user_choice == "Камень" and bot_choice == "Ножницы":
        result = "Победа!"
    elif user_choice == "Ножницы" and bot_choice == "Бумага":
        result = "Победа!"
    elif user_choice == "Бумага" and bot_choice == "Камень":
        result = "Победа!"
    elif user_choice == bot_choice:
        result = "Ничья"
    else:
        result = "Поражение"

    await message.answer(
        f"Ваш выбор: {user_choice}\nВыбор бота: {bot_choice}\nРезультат: {result}",
        reply_markup=rps_menu
    )

@dp.message_handler(lambda message: message.text == "Рандомайзер")
async def randomizer(message: types.Message):
    random_value = random.randint(1, 100) 
    await message.answer(f"Случайное число: {random_value}")


@dp.message_handler(lambda message: message.text == "Назад")
async def back_to_main_menu(message: types.Message):
    await message.answer(
        "Выберите, что вы хотите сделать:",
        reply_markup=start_menu
    )



if __name__ == "__main__":

    asyncio.run(dp.start_polling())

