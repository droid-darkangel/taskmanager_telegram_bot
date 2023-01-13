from aiogram import types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import logging
import asyncio
import random

import buttons as btns
import telegram_database as db_task
from config import *


db = db_task.Database('telegram_database.db')
logging.basicConfig(level=logging.INFO)


class Date_Task_Todo(StatesGroup):
    date = State()
    task = State()

class Show_Todo(StatesGroup):
    date = State()

class Delete_tasks(StatesGroup):
    date = State()



async def add_todo(user_id):
    await bot.send_message(user_id, text='Введите название задачи: ')
    await Date_Task_Todo.task.set()
@dp.message_handler(state=Date_Task_Todo.task)
async def add_todo_task(msg: types.Message, state:FSMContext):
    text = msg.text

    await state.update_data(task=text)

    await msg.answer('Введите дату выполнения: ')
    await Date_Task_Todo.date.set()
@dp.message_handler(state=Date_Task_Todo.date)
async def add_todo_full(msg:types.Message, state:FSMContext):
    date = msg.text.lower()
    user_id = msg.chat.id
    data = await state.get_data()

    task = str(data.get('task'))

    await db.add_tasks(user_id,date,task)
    await msg.answer('Задача успешно добавлена!')

    await state.reset_state(with_data=False)



async def show_todo(user_id):

    dates = set(await db.get_dates(user_id))

    await bot.send_message(user_id, 'Доступные даты:')
    for i in dates:
        await bot.send_message(user_id, i[0])

    await asyncio.sleep(2)
    await bot.send_message(user_id, 'Введите дату: ')
    await Show_Todo.date.set()
@dp.message_handler(state=Show_Todo.date)
async def show_todo_full(msg: types.Message, state: FSMContext):
    user_id = msg.chat.id
    date = msg.text.lower()

    tasks = set(await db.get_task(user_id, date))

    for i in tasks:
        await msg.answer(i[0])    
    await state.reset_state(with_data=False)



async def delete_tasks(user_id):
    dates = set(await db.get_dates(user_id))

    await bot.send_message(user_id, 'Доступные даты для удаления:')
    for i in dates:
        await bot.send_message(user_id, i[0])

    await asyncio.sleep(2)
    await bot.send_message(user_id, 'Введите дату: ')

    await Delete_tasks.date.set()
@dp.message_handler(state=Delete_tasks.date)
async def delete_tasks_full(msg: types.Message, state: FSMContext):
    user_id = msg.chat.id
    date = msg.text.lower()

    await db.delete_tasks(user_id,date)
    await msg.answer('Задачи по этой дате успешно удалены!')
    await state.reset_state(with_data=False)



async def rand_task(user_id):

    task = random.choice(random_task)
    await db.add_tasks(user_id,'сегодня',task)

    await bot.send_message(user_id, 'Задача успешно добавлена!')



@dp.message_handler(commands=['start'])
async def main(msg: types.Message):
    await msg.answer(help_text, reply_markup=btns.main_menu())



#обработчик команд
@dp.message_handler()
async def menu(msg:types.Message):
    user_id = msg.chat.id
    text_msg_lower = msg.text.lower()[2:]


    if text_msg_lower == 'помощь':
        await msg.answer(help_text)
    
    elif text_msg_lower == 'добавить':
        await add_todo(user_id)
    elif text_msg_lower == 'показать':
        await show_todo(user_id)
    elif text_msg_lower == 'удалить':
        await delete_tasks(user_id)
    elif text_msg_lower == 'рандом':
        await rand_task(user_id)
    else:
        await bot.send_message(user_id, 'Я тебя не понимаю...')




executor.start_polling(dp, skip_updates=True)