import data
from aiogram import  Bot , Dispatcher 

TOKEN = "BOT_TOKEN"
connection = data.create_connection('data.sql')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
