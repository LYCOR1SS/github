import logging

from aiogram import Bot, Dispatcher, executor, types
# from tugmalar import mars_shop_inline,mars_menu,mars_profile_inline

API_TOKEN = '6220529358:AAFrf1XAUcNJR4vI-si4BKgzUXxBZK5dFXI'


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def echo(message: types.Message):
    await message.answer("Siz gif jo'natdingiz")


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo(message: types.Message):
    await message.answer("Siz stiker jo'natdingiz")


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def echo(message: types.Message):
    await message.answer("Siz audio jo'natdingiz")


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def echo(message: types.Message):
    await message.answer("Siz contact jo'natdingiz")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def echo(message: types.Message):
    await message.answer("Siz photo jo'natdingiz")



@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def echo(message: types.Message):
    await message.answer("Siz video jo'natdingiz")

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def echo(message: types.Message):
    await message.answer("Siz locatciya jo'natdingiz")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)