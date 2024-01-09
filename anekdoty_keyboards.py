from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


ikb = InlineKeyboardMarkup(row_width=2, )
ib1 = InlineKeyboardButton(text='Детские', callback_data='Детские')
ib2 = InlineKeyboardButton(text='Про программистов', callback_data='Про программистов')
ib3 = InlineKeyboardButton(text='Короткие', callback_data='Короткие')
ib4 = InlineKeyboardButton(text='Тупые но смешные', callback_data='Тупые, но смешные')
ib5 = InlineKeyboardButton(text='Про жену', callback_data='Про жену')
ib6 = InlineKeyboardButton(text='Для взрослых', callback_data='Для взрослых')
ib7 = InlineKeyboardButton(text='Разные анекдоты', callback_data='Разные анекдоты')
ib8 = InlineKeyboardButton(text='Анекдоты про Вовочку', callback_data='про Вовочку')
ib9 = InlineKeyboardButton(text='Анекдоты про подростков', callback_data='про подростков')
ikb.add(ib1, ib2, ib3, ib4, ib5, ib6, ib7, ib8, ib9,)

like_keyboard=InlineKeyboardMarkup(row_width=2)
like = InlineKeyboardButton(text='👍', callback_data='like')
dislike = InlineKeyboardButton(text='👎', callback_data='dislike')
like_keyboard.add(like, dislike)
