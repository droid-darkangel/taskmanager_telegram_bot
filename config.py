from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '5926314262:AAFnt5SzZg3Z47_ShHZctkyQbpSqrq1dQpQ'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


random_task = ["Выпить стакан воды",
                "Отжаться 5 раз",
                "Покормить кошку",
                "Помыть машину",
                "Сделать все домашнее задание",
                "Убраться в комнате",
                "Учить Python",
                "Погулять с собакой",
                "Покушать",
                "Не опоздать на занятия"
                ] 

help_text = """ 
помощь - напечатать справку по программе.
добавить - добавить задачу в список.
показать - напечатать все добавленные задачи.
удалить - удалить задачи.
рандом - добавить случайную задачу на дату сегодня
выход - выход.
"""
    