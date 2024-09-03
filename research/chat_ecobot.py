import logging 
from aiogram import Bot, Dispatcher, executor,types
from dotenv import load_dotenv
import os

load_dotenv()
API=os.getenv("TOKEN")
#print(API)

logging.basicConfig(level=logging.INFO)


# initalize bot and dispatcher
bot=Bot(token=API)
dp=Dispatcher(bot)  #It is used to make the connection with the bot

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply("Hi\nI am Echo Bot!\n Powered by Athrva Bhawsar")

@dp.message_handler()
async def echo(message: types.Message): #async is taking the input that we provided
    """
    This will return echo
    """
    
    await message.answer(message.text)
        
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
    
# Now implement Open AI with the bot     



