from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
import config.config as cfg
import config.bad_words as bw

bot = Bot(token=cfg.token_tg_bot)
dp = Dispatcher(bot)

# test 11


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Я домовенок! Главный в доме! Как решу- так и будет! В моём доме- не выражаться!!!! Добавь меня в чат, где нужно наводить порядок, на правах админа!")


@dp.message_handler(commands=['тест'], commands_prefix="!")
async def add_svoi(message: types.Message):
    await message.answer("ТЕСТ")


@dp.message_handler()
async def mess_handler(message: types.Message):
    text = message.text.lower()
    for word in bw.WORDS:
        if word in text:
            await message.delete()


@dp.message_handler(content_types=["left_chat_member"])
async def start_commandr(message: types.Message):
    await message.answer("Ливнул, ширый...\n🤷‍♀️Чё приходил этот недопатриот....🤷🏻‍♂️")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
