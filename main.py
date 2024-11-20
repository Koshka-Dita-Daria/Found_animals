from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import asyncio
import os
# from decouple import config
# from easy_async_tg_notify import Notifier
text_info = "Здравствуйте, этот бот для поиска потерянных питомцев, которые есть в нашей базе данных. Если вы хотите найти вашего друга или вы нашли чужого домашнего животного, то нажмите на кнопку вернуться"

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

empty_kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb = InlineKeyboardMarkup()
KeyboardButton1 = InlineKeyboardButton(text='Вернуться', callback_data="back")
kb.add(KeyboardButton1)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)


InlineButton1 = KeyboardButton(text='Информация о боте.')
InlineButton2 = KeyboardButton(text='Бланк о потерянном животном')
InlineButton3 = KeyboardButton(text='Для тех, кто нашел животное')
kb1.add(InlineButton1, InlineButton2, InlineButton3)


@dp.message_handler(commands=['start', 'help'])
async def start(message):
    await message.answer("Привет! Я бот, который помогает в поиске потерянных животных.", reply_markup=kb1)


@dp.message_handler(text="Информация о боте.")
async def main_menu(message):
    await message.answer(text_info, reply_markup=empty_kb)
    await message.answer(text_info, reply_markup=kb1)


@dp.callback_query_handler(text=["back"])
async def callback_inline(call):
    await call.message.answer('Вы вернулись в главное меню', reply_markup=kb1)
    await call.answer()


@dp.message_handler()
async def other(message):
    await message.answer("Введите команду /start или /help, чтобы начать общение")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)