import data
from config import bot, dp, connection
from aiogram import  executor, types


@dp.message_handler(commands=['db'])
async def echo(message:types.Message):
	select_users = "SELECT * from users"
	users = data.execute_read_query(connection, select_users)
	for user in users:
	    await message.answer(user)


@dp.message_handler(commands=['cs'])
async def echo(message:types.Message):
	counts = data.read_all(connection)
	for count in counts:
		data.update_status(connection, count[0],0)


@dp.message_handler(commands=['cc'])
async def echo(message:types.Message):
	counts = data.read_all(connection)
	for count in counts:
		data.update_companion(connection, count[0], 0)


@dp.message_handler(commands=['ss'])
async def echo(message:types.Message):
	counts = data.read_all(connection)
	for count in counts:
		# data.update_status(connection, count[0])
		data.update_subscribe(connection, count[0], 1)


@dp.message_handler(lambda message: message.text.startswith('set'))
async def echo(message:types.Message):
	ident = int(message.text.split('_')[1])
	value = int(message.text.split('_')[2])
	data.set_new_user(connection, ident ,value)
	await message.answer(ident)


@dp.message_handler(lambda message: message.text.startswith('upd'))
async def echo(message:types.Message):
	ident = int(message.text.split('_')[1])
	value = int(message.text.split('_')[2])
	data.update_status(connection, ident ,value)
	await message.answer(ident)
