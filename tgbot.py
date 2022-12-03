from aiogram import Bot, Dispatcher, executor, types

API = ''
CHANNEL_ID = ''

bot = Bot(token=API)
dp = Dispatcher(bot)


# hello message
@dp.message_handler(commands =['start'])
async def hello(message: types.message):
    await message.reply(f'''hi, it's bot for transfer message to group''')
        
@dp.message_handler()
async def all_msg_handler(message: types.message):
    await bot.send_message(CHANNEL_ID, f'text: {message.text}\n username: {message.chat}')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    


