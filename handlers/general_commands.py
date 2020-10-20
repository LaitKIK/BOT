import asyncio
from aiogram import types
from misc import dp, admin
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from .states import Form
from aiogram.types import ReplyKeyboardMarkup, \
                          KeyboardButton
button_track1 = KeyboardButton('Сингл — 300₽')
button_track2 = KeyboardButton('EP (до 7 треков) — 700₽')
button_track3 = KeyboardButton('Альбом (от 8 треков) — 900₽')

murkup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_track1).row(button_track2, button_track3)

button_track4 = KeyboardButton('Да')
button_track5 = KeyboardButton('Нет')

murkup2 =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_track4, button_track5)


button_track6 = KeyboardButton('BOOM/VK')
button_track7 = KeyboardButton('Apple Music')
button_track8 = KeyboardButton('Spotify')
button_track9 = KeyboardButton('Яндекс.Музыка')
button_track10 = KeyboardButton('Deezer')

murkup3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_track6).row(button_track7, button_track8).row(button_track9, button_track10)

button_track11 = KeyboardButton('Дизайн')
button_track12 = KeyboardButton('Годовая подписка')
button_track13 = KeyboardButton('Анимированная обложка')
button_track14 = KeyboardButton('Таргетированная реклама')

murkup4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_track11).row(button_track12, button_track13).add(button_track14)

button_track15 = KeyboardButton('На всех площадках')
button_track16 = KeyboardButton('Только в BOOM')
button_track17 = KeyboardButton('Везьде кроме BOOM')

murkup5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_track15, button_track16, button_track17)
                                                                                                                        
button_track18 = KeyboardButton('Увидел(-а) рекламу в Instagram')
button_track19 = KeyboardButton('Увидел(-а) рекламу в VK')
button_track20 = KeyboardButton('Посоветовали знакомые')
button_track21 = KeyboardButton('Нашел в поисковике')

murkup6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_track18, button_track19).row(button_track20, button_track21)


@dp.message_handler(commands=['cancel'], state='*')
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Действие отменено, анкета удалена')
    await message.forward(admin, disable_notification=None)
     

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await message.answer("*Тебя приветствует лейбл VisualCartel BOT.* \n\
                           Введи */info* что бы узнать информацию о публикации! \n\
                           Что бы узнать команды на которые я могу ответить, введи */help* ", parse_mode='MARKDOWN')
    

@dp.message_handler(commands=['info'], state='*')
async def info(message: types.message, state: FSMContext):
    await message.answer('*Внимание!*\n\
                        - Публикация релизов происходит в 00:00 на указанную дату\n\
                        - Рекомендуем присылать релизы за 7 рабочих дней до даты публикации\n\
                        - Аудио-файлы должны быть в формате mp3 или wav\n\
                        - Размер обложки не имеет значения, мы редактируем весь материал под формат площадок\n\n\
                         *Чтобы начать заполнение заявки, введите* /go ',  parse_mode='MARKDOWN')


@dp.message_handler(commands='help', state='*')
async def finaly_message(message: types.Message):
    await message.answer('*Бот может ответить на следующие команды*:\
                               \n\
                               \n */info* - информация о публикации; \
                               \n */go* - начало заполнения анкеты;\
                               \n */cover* - прикрепить обложку;\
                               \n */audio* - прикрепить трек(-и);\
                               \n */cancel* - отмена заявки;\
                               \n */submit* - завершить создание заявки.', parse_mode='MARKDOWN')
    

@dp.message_handler(commands='submit', state='*')
async def end_application(message: types.Message):
    await message.answer('*Ваша заявка принята, в ближайшее время с вами свяжется наш менеджер!*', parse_mode='MARKDOWN')
    

@dp.message_handler(commands='cover')
async def cover_message(message: types.Message):
    await message.answer('*Прикрепите обложку релиза!*\
                        \n\
                        \nПри отправлении выберите *"Отправить как фото"*', parse_mode='MARKDOWN')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def forward_cover(message: types.Message):
    await message.forward(admin, disable_notification=None)
    await message.answer('*Для завершения заявки впишите /submit*\
                        \nЧтобы прикрепить вашу композицию введите команду */audio*', parse_mode='MARKDOWN')




    
