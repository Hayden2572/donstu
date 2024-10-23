from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import db
import answer
import kb

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Хочешь узнать свой ID?", reply_markup=kb.menu)

@router.message(F.text == 'Узнать ID')
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID - {msg.from_user.id}")
    print(f"Incoming text - {msg.text}")
    
@router.message(F.text == "Нагрубить")
async def say_rude(msg: Message):
    await msg.answer(answer.say_rude, reply_markup=kb.menu)
    print(f"Incoming text - {msg.text}")
    
@router.message(F.text == "Извиниться")
async def say_rude(msg: Message):
    await msg.answer(answer.apologize, reply_markup=kb.menu)
    print(f"Incoming text - {msg.text}")

@router.message(F.text == "Посмотреть данные в базе данных")
async def show_db(msg: Message):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM database.usr_info")
    db.connection.commit()
    result = cursor.fetchall()
    text_result = ''
    for i in result:
        for j in i:
            text_result += str(j) + '  '
        text_result += "\n"
    print(result)
    await msg.answer(text_result, reply_markup=kb.menu)
    print(f"Incoming text - {msg.text}")

    #Здарова хуй