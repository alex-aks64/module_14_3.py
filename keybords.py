from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


ikb=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Product1',callback_data="product_buying"),
    InlineKeyboardButton(text='Product2',callback_data="product_buying"),
    InlineKeyboardButton(text='Product3',callback_data="product_buying"),
    InlineKeyboardButton(text='Product4',callback_data="product_buying")]])



kb=ReplyKeyboardMarkup(keyboard=[
                                 [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
                                 [KeyboardButton(text='Купить')]], resize_keyboard=True,)













