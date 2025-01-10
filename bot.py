from aiogram import Bot, Dispatcher, executor, types
from translate import translate_website

API_TOKEN = 7865837029:AAEBwuh5CoHw7HG5OfWfWwkdI6cVDOtvb10

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Send a website URL to translate it into multiple languages.")

@dp.message_handler(content_types=['text'])
async def handle_url(message: types.Message):
    url = message.text
    await message.reply("Processing the website...")
    
    try:
        languages = translate_website(url)
        response = "Website has been translated into the following languages:\n" + "\n".join(languages)
        await message.reply(response)
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
