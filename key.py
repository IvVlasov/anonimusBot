from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton
import qiwi
def main_menu():
	menu =ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
	a1 = KeyboardButton('🎲 Поиск собеседника')
	a3 = KeyboardButton('🚻 Поиск по полу')
	menu.row(a1)
	menu.row(a3)
	return menu

##### FIND BY GENDER #####
def genderMenu():
	menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
	man = KeyboardButton('Мужской')
	woman = KeyboardButton('Женский')
	menu.add(man).add(woman)
	return menu

def stop():
	menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
	item1 = KeyboardButton('Отменить поиск')
	menu.add(item1)
	return menu

##### MENU WHEN CHATING #####
def secondMenu():
	menu =ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
	item1 = KeyboardButton('Новый собеседник')
	item2 = KeyboardButton('Стоп')
	menu.add(item1).add(item2)
	return menu

##### MENU WHEN CHATING #####
def genderButtons():
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	man = InlineKeyboardButton( text='Мужской', callback_data='gender_2')
	woman = InlineKeyboardButton( text='Женский', callback_data='gender_3')
	menu.add(man).add(woman)
	return menu

def buyButton():
	bill = qiwi.generate_billID(50)
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	item = InlineKeyboardButton( text='7 дней - 59 рублей', callback_data='payment_1')
	item = InlineKeyboardButton( text='1 месяц - 199 рублей', callback_data='payment_2')
	item = InlineKeyboardButton( text='6 месяцев - 599 рублей', callback_data='payment_3')
	menu.add(item)
	return menu








