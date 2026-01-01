# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть доступ", callback_data="open")
    )

    await bot.send_message(
        update.from_user.id,
        "Чтобы открыть доступ, подтвердите действие 👇",
        reply_markup=keyboard
    )

@dp.callback_query_handler(lambda c: c.data == "open")
async def approve(callback: types.CallbackQuery):
    await bot.approve_chat_join_request(
        chat_id=CHANNEL_ID,
        user_id=callback.from_user.id
    )

    await bot.send_message(
        callback.from_user.id,
        "🎁 Основное предложение:\n\n(тут будет твой оффер)"
    )

    await callback.answer("Доступ открыт")

executor.start_polling(dp)

