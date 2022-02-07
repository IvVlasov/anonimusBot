import data
import random
import key
from config import bot, dp, connection
from aiogram import  executor, types


@dp.callback_query_handler(lambda c: c.data.startswith('gender'))
async def set_user(call):
	value = int(call.data.split('_')[1])
	if data.find_chat_id(connection, call.message.chat.id) == 'ERROR':
		data.set_new_user(connection, call.message.chat.id, value)
	else:
		await call.message.answer('Выбери что тебе нужно',
										  reply_markup=key.main_menu())


@dp.message_handler(lambda message: message.text == '🚻 Поиск по полу')
async def findByGender(message:types.Message):
	await message.answer('Какой пол будем искать?',
								reply_markup = key.genderMenu())


@dp.message_handler(lambda message: message.text == '🎲 Поиск собеседника')
async def findChat(message:types.Message):
	data.update_status(connection, message.chat.id,1)
	if data.search_active_status(connection,message.chat.id, 1) == []  and\
			data.search_active_status(connection,message.chat.id,
		  data.read_gender(connection,message.chat.id)) == []:
		await message.answer('Подождите',reply_markup=key.stop())
	else:
		item1 = data.search_active_status(connection,message.chat.id, 1)
		item2 = data.search_active_status(connection,message.chat.id,
													 data.read_gender(connection,message.chat.id))
		# item3 = data.search_active_status(connection,message.chat.id, 3)
		# await message.answer(item2)
		count = item1 + item2
		value = random.randint(0, len(count) - 1)
		companion_id = count[value][0]
		data.update_status(connection, message.chat.id,0)
		data.update_status(connection, companion_id,0)
		data.update_companion(connection, message.chat.id, companion_id)
		data.update_companion(connection, companion_id, message.chat.id)	
		
		await message.answer('Собеседник найден', reply_markup =key.secondMenu())
		await bot.send_message(companion_id, text= 'Собеседник найден',
									  reply_markup =key.secondMenu())


@dp.message_handler(lambda message: message.text == 'Стоп')
async def stopChat(message:types.Message):
	companion_id = data.read_companion(connection, message.chat.id)
	data.update_companion(connection, message.chat.id, 0)
	data.update_companion(connection, companion_id, 0)
	await message.answer('Чат остановлен', reply_markup = key.main_menu())
	await bot.send_message(companion_id, text= 'Чат остановлен',
								  reply_markup =key.main_menu())


@dp.message_handler(lambda message: message.text == 'Мужской')
async def findNewChat(message:types.Message):
	if data.read_subscribe(connection, message.chat.id) == 0:
		await message.answer('Для поиска по полу необходима подписка',
									reply_markup= key.buyButton())
	else:
		data.update_status(connection, message.chat.id,2)
		if data.search_active_gender(connection,message.chat.id, 2, 1) == [] and\
				data.search_active_gender(connection,message.chat.id, 2,
					data.read_gender(connection,message.chat.id)) == []:
			await message.answer(data.read_gender(connection,message.chat.id),
										reply_markup=key.stop())
		else:
			list1 = data.search_active_gender(connection,message.chat.id,2 ,1)
			list2 = data.search_active_gender(connection,message.chat.id, 2,
														 data.read_gender(connection,message.chat.id))
			count = list1 + list2

			value = random.randint(0, len(count) - 1)
			companion_id = count[value][0]

			data.update_status(connection, message.chat.id,0)
			data.update_status(connection, companion_id,0)
			data.update_companion(connection, message.chat.id, companion_id)
			data.update_companion(connection, companion_id, message.chat.id)	
			
			await message.answer('Собеседник найден', reply_markup =key.secondMenu())
			await bot.send_message(companion_id, text= 'Собеседник найден',
										  reply_markup =key.secondMenu())


@dp.message_handler(lambda message: message.text == 'Женский')
async def findNewChat(message:types.Message):
	if data.read_subscribe(connection, message.chat.id) == 0:
		await message.answer('Поиск по полу доступен только премиум подписчикам.'
									' \n Для продолжения вам необходимо оплатить подписку.',
									reply_markup= key.buyButton())
	else:
		data.update_status(connection, message.chat.id,3)
		if data.search_active_gender(connection,message.chat.id, 3, 1) == [] and\
				data.search_active_gender(connection,message.chat.id, 3,
				data.read_gender(connection,message.chat.id)) == []:
			await message.answer(data.read_gender(connection,message.chat.id),
										reply_markup=key.stop())
		else:
			list1 = data.search_active_gender(connection,message.chat.id,3 ,1)
			list2 = data.search_active_gender(connection,message.chat.id, 3,
											data.read_gender(connection,message.chat.id))
			count = list1 + list2
			value = random.randint(0, len(count) - 1)
			companion_id = count[value][0]

			data.update_status(connection, message.chat.id,0)
			data.update_status(connection, companion_id,0)
			data.update_companion(connection, message.chat.id, companion_id)
			data.update_companion(connection, companion_id, message.chat.id)	
			
			await message.answer('Собеседник найден', reply_markup =key.secondMenu())
			await bot.send_message(companion_id, text= 'Собеседник найден',
										  reply_markup =key.secondMenu())


@dp.message_handler(lambda message: message.text == 'Новый собеседник')
async def findNewChat(message:types.Message):
	await stopChat(message)
	await findChat(message)


@dp.message_handler(lambda message: message.text == 'Отменить поиск')
async def findNewChat(message:types.Message):
	data.update_status(connection, message.chat.id, 0)
	await message.answer('Поиск остановлен', reply_markup = key.main_menu())


@dp.callback_query_handler(lambda c: c.data.startswith('payment'))
async def chek_payment(call):
	value = call.data.split('_')[1]
	await call.message.answer('PAy')




