import aioredis
import asyncio
import logging
from aiogram import types
from misc import dp, bot, admin
from .general_commands import murkup1, murkup2, murkup3, murkup4, murkup5, murkup6
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext
from .states import Form


@dp.message_handler(commands='go', state=None)
async def filling(message: types.Message, state = FSMContext):
    await message.answer("*Сколько треков требуется опубликовать?*", reply_markup=murkup1, parse_mode='MARKDOWN')
    await Form.state_1.set() 


@dp.message_handler(state=Form.state_1)
async def name_release(message: types.Message, state: FSMContext):
    filling = message.text
    await state.update_data(filling1=filling)
    await message.answer("*Укажите имя исполнителя и название релиза*\
                        \n\
                        \nВ совместных релизах указывайте исполнителей через запятую или feat.\
                        \nПример: KILLAH - Nonsense", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_2)
async def dowload_release(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name1=name)
    await message.answer("*Загрузите треки из релиза через dropmefiles.com *\
                        \nЕсли вы хотите прикрепить трек прямиков в ТГ, введите '-' \
                        \n\
                        \nТреки должны быть подписаны по форме:\
                        \n#трека.Никнейм-Название-Битмейкер\
                        \n\
                        \n1. Перейдите на сайт https://dropmefiles.com/\
                        \n2. Перетяните папку или архив с файлами\
                        \n3. Дождитесь завершения загрузки\
                        \n4. Скопируйте появившуюся внизу страницы ссылку и вставьте в поле ниже\
                        \n\
                        \nТреки также можно загрузить на Яндекс.Диск, либо любое другое облачное хранилище", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_3)
async def bad_words(message: types.Message, state: FSMContext):
    download = message.text
    await state.update_data(download1=download)
    await message.answer('*Укажите в каких треках есть ненормативная лексика*\
                        \n\
                        \nЕсли в треках нет ненормативной лексики, поставьте \"-\"\
                        \nПример: 1, 2, 3 и т.д.', parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_4)
async def genre_release(message: types.Message, state: FSMContext):
    bad_word_track = message.text
    await state.update_data(bad_word_track1 = bad_word_track)
    await message.answer('*Укажите жанр релиза*\
                        \n\
                        \nПример: хип-хоп / рэп / альтернатива и т.д.', parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_5)
async def time_code(message: types.Message, state: FSMContext):
    genre = message.text
    await state.update_data(genre1=genre)
    await message.answer("*Укажите таймкод треков для TikTok*\
                        \n\
                        \nНе обязательно. Максимум 15 секунд.\
                        \nПример: 1) 00:05-00:20 2) 00:10-00:25 и т.д.", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_6)
async def bitmake(message: types.Message, state: FSMContext):
    time_code_track = message.text
    await state.update_data(time_code_track1=time_code_track)
    await message.answer("*Требуется указать битмейкера?*", reply_markup=murkup2, parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_7)
async def date(message: types.Message, state: FSMContext):
    bitmake_track = message.photo
    await state.update_data(bitmake_track1=bitmake_track)
    await message.answer("*Введите дату релиза*\
                        \n\
                        \nПример: день-месяц-год", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_8)
async def cart(message: types.Message, state: FSMContext):
    date_release = message.text
    await state.update_data(date_release1=date_release)
    await message.answer('*Заполнение карточки музыканта* \
                        \n\
                        \nДля указания более одного значения, введите данные письменно. \
                        \nЕсли не требуются, поставте "-"\
                        \n\
                        \nВ заполнение карточки музыканта входит добавление фото, привязка к сообществу и верификация (галочка)\
                        \n1 карточка — 400₽, 2 карточки — 600₽, 3 карточки — 900₽, 4 карточки — 1200₽, все карточки — 1500₽', reply_markup=murkup3, parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_9)
async def dop_services(message: types.Message, state: FSMContext):
    cart_musition = message.text
    await state.update_data(cart_musition1=cart_musition)
    await message.answer('*Дополнительные услуги*\
                        \n\
                        \nДля указания более одного значения, введите данные письменно.\
                        \nЕсли не требуются, поставте "-"\
                        \n\
                        \nДанные по услугам уточнит менеджер', reply_markup=murkup4, parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_10)
async def publish(message: types.Message, state: FSMContext):
    additional_services = message.text
    await state.update_data(additional_services1=additional_services)
    await message.answer("*Где публикуем релиз?*", reply_markup=murkup5, parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_11)
async def here(message: types.Message, state: FSMContext):
    publish_releases = message.text
    await state.update_data(publish_releases1=publish_releases)
    await message.answer("*Откуда вы о нас узнали?*", reply_markup=murkup6, parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_12)
async def comment(message: types.Message, state: FSMContext):
    here_about = message.text
    await state.update_data(here_about1=here_about)
    await message.answer("*Комментарий к заявке*\
                        \n\
                        \nПожелания и коментарий к публикации.", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_13)
async def link(message: types.Message, state: FSMContext):
    comment_aplication = message.text
    await state.update_data(comment_aplication1=comment_aplication)
    await message.answer("*Укажите ссылку на вашу страницу в VK*", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_14)
async def mail(message: types.Message, state: FSMContext):
    link_VK = message.text
    await state.update_data(link_VK1=link_VK)
    await message.answer("*Укажите вашу почту*", parse_mode='MARKDOWN')
    await Form.next()


@dp.message_handler(state=Form.state_15)
async def Cover_release(message: types.Message, state: FSMContext):
    you_mail = message.text
    await state.update_data(you_mail1=you_mail)
    await message.answer("*Прикрепите обложку релиза*\
                        \n\
                        \nЧтобы прикрепить обложку введите команду /cover", parse_mode='MARKDOWN')
    data = await state.get_data()
    filling1 = data.get('filling1')
    name1 = data.get('name1')
    download1 = data.get('download1')
    bad_word_track1 = data.get('bad_word_track1')
    genre1 = data.get('genre1')
    time_code_track1 = data.get('time_code_track1')
    bitmake_track1 = data.get('bitmake_track1')
    date_release1 = data.get('date_release1')
    cart_musition1 = data.get('cart_musition1')
    additional_services1 = data.get('additional_services1')
    publish_releases1 = data.get('publish_releases1')
    here_about1 = data.get('here_about1')
    comment_aplication1 = data.get('comment_aplication1')
    link_VK1 = data.get('link_VK1')
    you_mail1 = message.text

    await bot.send_message(admin, f'*Количество треков для публикации:* {filling1}\n'
                                  f'*Имя исполнимеля и название релиза:* {name1}\n'
                                  f'*Ссылка на dropmefiles.com:* {download1}\n'
                                  f'*В каких треках есть нецензурная лексика:* {bad_word_track1}\n'
                                  f'*Жанр релиза:* {genre1}\n'
                                  f'*Тайм код Тик-Ток:* {time_code_track1}\n'
                                  f'*Указать битмейкера:* {bitmake_track1}\n'
                                  f'*Указать дату релиза:* {date_release1}\n'
                                  f'*Карточка музыканта:* {cart_musition1}\n'
                                  f'*Дополнительные услуги:* {additional_services1}\n'
                                  f'*Где публикуются релизы:* {publish_releases1}\n'
                                  f'*Откуда вы о нас узнали:* {here_about1}\n'
                                  f'*Коментарий:* {comment_aplication1}\n'
                                  f'*Ссылка ВК:* {link_VK1}\n'
                                  f'*Эмэйл:* {you_mail1}', parse_mode='MARKDOWN')
    await state.reset_state(with_data=False)


@dp.message_handler(state='*', commands='audio')
async def audio_forwa(message: types.message):
    await message.answer('*Прикрепите аудио файл* \
                         \n\
                         \n*Предупреждение* - если ВЫ отсылаете более одного трека, делайте это одним сообщением!', parse_mode='MARKDOWN')


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def forward_aaw(message: types.message):
    await message.forward(admin, disable_notification=None)
    await message.answer('*Для подачи заявки введите /submit*', parse_mode='MARKDOWN')