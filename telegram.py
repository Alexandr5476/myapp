import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def fnc(text):
    ses = await bot.get_session()
    await bot.send_message(chat_id="888281527", text=text)
    await ses.close()


def send(text):
    if text != '':
        asyncio.run(fnc(text))
