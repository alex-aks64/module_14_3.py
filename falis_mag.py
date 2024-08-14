from mailbox import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import texts
from keybords import *

APM="7298843250:"
bot=Bot(token=APM)
dp=Dispatcher(bot,storage= MemoryStorage())


@dp.message_handler(text=['start','/start'])
async def start(message):
    print(f'Мы получили собщение {message.text} ')
    with open('1.jpg',"rb") as j:
        await message.answer_photo(j,texts.b, reply_markup=kb)



@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for i in range(1,5):
        product_info = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.answer(product_info)
        with open(f'5.jpg', "rb") as j:
            await message.answer_photo(j)
    await message.answer(texts.b2,reply_markup=ikb)



@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
        await call.message.answer(texts.b3)
        await call.answer()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)