import datetime
import time

from aiogram import executor, Bot, Dispatcher, types
from anekdoty_keyboards import ikb, like_keyboard

from anekdoty import get_joke

TOKEN_API = 'YOUR_BOT_TOKEN'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


# Печать сообщения о запуске бота
async def on_startup(_):
    print('Бот был успешно запущен')


with open('../logging.txt', 'a', encoding='utf-8') as file:
    # Обработчик команды /start
    @dp.message_handler(commands=['start'])
    async def start_command(message: types.Message):
        await message.reply(text="Привет! Все анекдоты беруться в онлайн режиме с сайта anekdoty.ru. Выбери категорию и получи анекдот.", reply_markup=ikb)
        file.write(f"ПОЛЬЗОВАТЕЛЬ id={message.chat.id} username={message.chat.username} ЗАПУСТИЛ БОТА В  {str(datetime.datetime.now())[:20]} \n")

    #Отправляет сообщение пользователю после отправки анекдота
    @dp.message_handler()
    async def one_more_joke(message: types.Message=None,chat_id=None, text_message=None ):
        if message:
            text=message.text
            user = message.from_user
            print(f"{user} отправил {text}")
            file.write(f"Пользователь с id={user.id} username={user.username} first_name={user.first_name} отправил сообщение {text} \n")
            await bot.send_message(chat_id=message.chat.id, text='Выберите категорию анекдота по кнопке', reply_markup=ikb)
        elif text_message=='dislike':
            text='Давайте выберем еще один анекдот, он точно понравится :)'
            await bot.send_message(chat_id=chat_id, text=text, reply_markup=ikb)
        elif text_message=='like':
            text='Отлично! Посмеемся еще?'
            await bot.send_message(chat_id=chat_id, text=text, reply_markup=ikb)


    #Обработчик кнопок инлайн клавиатуры
    @dp.callback_query_handler()
    async def joke_callback(callback: types.CallbackQuery):
        chat_id = callback.message.chat.id
        if callback.data=='dislike':
            await callback.answer('Жаль, что не понравилась шутка')
            file.write((f"user_id={callback.from_user.id} username={callback.from_user.username} поставил дизлайк \n"))
            await one_more_joke(chat_id=chat_id, text_message='dislike')  # Вызывает функцию, которая предлагает выбрать еще 1 анекдот
        elif callback.data=='like':
            await callback.answer('Здорово! Анекдот зашёл!')
            file.write((f"user_id={callback.from_user.id} username={callback.from_user.username} поставил лайк \n"))
            await one_more_joke(chat_id=chat_id, text_message='like')  # Вызывает функцию, которая предлагает выбрать еще 1 анекдот
        else:
            text=get_joke(callback.data)
            await bot.send_message(chat_id=chat_id, text=text) #Отправляет анекдот
            file.write(f"Время отправки={str(datetime.datetime.now())[:20]} user_id={callback.from_user.id} username={callback.from_user.username} текст анекдота={text} \n")
            await bot.send_message(chat_id=chat_id, text="Как вам анекдот?", reply_markup=like_keyboard)
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)  # Удаляет последнее сообщение с клавиатурой


    # Запуск бота
    if __name__ == '__main__':
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
