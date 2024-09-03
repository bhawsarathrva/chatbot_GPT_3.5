from aiogram import Bot, Dispatcher, executor,types
from dotenv import load_dotenv
import openai
import sys
import os

class Reference:
    '''
    A class to store previously responce from the chatgpt API
    '''
    
    def  __init__(self) -> None:
        self.reference = ""

load_dotenv()
OpenAi_API_key=("OpenAI_API_KEY")

reference = Reference()

API=os.getenv("TOKEN")

#model name
MODEL_NAME ="gpt-3.5-turbo"

# initialize the bot and dispatcher
bot=Bot(token=API)
dp=Dispatcher(bot)

def clear_past():
    reference.response = ""
    
    
@dp.message_handler(commands=['start'])
async def Welcome(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply("Hi\nI am Chat Bot!\n Created by Athrva Bhawsar\n How can I assist you?")
    

@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I ve cleared the past conversation and context")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """ 
    A handler to display the help menu.
    """
    help_command = """
    Hi there I'm cahtgpt tele bot created by athrva Plz follow these commands-
    /start - To start the conversation
    /clear - to clear past convo
    /help - to get help
    """
    await message.reply(help_command)

@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME, #gpt_3.5_turbo
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)
   
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)