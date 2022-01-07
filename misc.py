import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admin='438808692'

bot = Bot(token='1218641102:AAGuRftfG3uvCwisvvfmwKMsydY3O-6oHbk')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
