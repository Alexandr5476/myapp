import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def fnc(text):
    await bot.send_message(chat_id="888281527", text=text)
    await bot.session.close()


def send(text):
    asyncio.run(fnc(text))
