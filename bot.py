from aiogram import  executor, types
from config import bot, dp, connection
from datetime import datetime, date, time
import logging 
import random
import data
import admin
import callbacks
import key


logging.basicConfig(level=logging.INFO)


def find_companion():
	count = data.search_active_status(connection)
	value = random.randint(0, len(count) - 1)
	result = count[value][0]
	return result


@dp.message_handler(commands=['start'])
async def echo(message:types.Message):
	await message.answer('Укажи свой пол', reply_markup=key.genderButtons())


@dp.message_handler(content_types=['photo'])
async def echo(message:types.Message):
	companion_id = data.read_companion(connection, message.chat.id)
	await bot.send_photo(companion_id, photo=message.photo[0].file_id)
	# await bot.send_message(companion_id, text= message.photo[0].file_id)


@dp.message_handler(lambda message: message.text)
async def echo(message:types.Message):
	companion_id = data.read_companion(connection, message.chat.id)
	if companion_id != 0:
		await bot.send_message(companion_id, text= message.text)
	else:
		dateWas = data.read_data(connection, message.chat.id)
		await message.answer(message.date.toordinal() - dateWas)


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)