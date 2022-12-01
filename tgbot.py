from aiogram import Bot, Dispatcher, executor, types

API = '5803797844:AAGbLCYGDvalfSh3rv-17e4dOD6Y2pVianc'
CHANNEL_ID = '-1001869477722'

bot = Bot(token=API)
dp = Dispatcher(bot)


# hello message
@dp.message_handler(commands =['start'])
async def hello(message: types.message):
    await message.reply(f'''
Здравствуйте!

Напишите, что хотите, и мы опубликуем его в нашем канале в ближайшие сроки.
 
Гарантируем анонимность🗣
                        ''')
        
@dp.message_handler()
async def all_msg_handler(message: types.message):
    await bot.send_message(CHANNEL_ID, f'text: {message.text}\n username: {message.chat}')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    


