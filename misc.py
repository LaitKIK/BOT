import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admin='438808692'

bot = Bot(token='1230290644:AAGqXueOOYrrVplM6Uol6Rv79ya362nsQ_M')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)