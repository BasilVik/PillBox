from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

import keyboard
import messages

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(messages.greet.format(
        name=msg.from_user.full_name),
        reply_markup=keyboard.menu)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(messages.menu, reply_markup=keyboard.menu)
