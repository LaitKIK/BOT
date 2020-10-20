from aiogram import executor, types, Bot
from misc import dp
import aioredis
import handlers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
