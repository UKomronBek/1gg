from aiogram import Router,F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile

from bot.api.bitcoin import get_bitcoin_course
from bot.config import SCHEDULE, group_students, books, SCHEDULE_2, SCHEDULE_1
from bot.keyboards.inline.panel_kb import main_panel_kb, group_panel_kb, schedule_students_panel, library_kb, \
    choose_schedule_kb, back_scheduler_panel

user_router = Router(name='user_router')


@user_router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('<b>⚙️Панель [1TN3]: </b>', reply_markup=main_panel_kb())


@user_router.callback_query(F.data == 'first_group')
async def first_group_btn(callback: CallbackQuery):
    await callback.message.edit_text('<b>⚙️Панель [1TN3]{A}: </b>', reply_markup=group_panel_kb(1))


@user_router.callback_query(F.data == 'second_group')
async def second_group_btn(callback: CallbackQuery):
    await callback.message.edit_text('<b>⚙️Панель [1TN3]{B}: </b>', reply_markup=group_panel_kb(2))


@user_router.callback_query(F.data.startswith('group_schedule__'))
async def send_group_schedule_btn(callback: CallbackQuery):
    number = callback.data[-1]
    await callback.message.edit_text("Выберите день недели: ", reply_markup=choose_schedule_kb(number))


@user_router.callback_query(F.data.startswith('scheduleday'))
async def send_day_schedule_btn(callback: CallbackQuery):
    data = callback.data.split('_')
    day, number = data[1], data[2]
    schedules = SCHEDULE_1 if number == '1' else SCHEDULE_2
    result = schedules[day]
    await callback.message.edit_text(result, reply_markup=back_scheduler_panel(number))


@user_router.callback_query(F.data.startswith('group_students__'))
async def send_group_students__btn(callback: CallbackQuery):
    number = callback.data[-1]
    await callback.message.edit_text(group_students[number], reply_markup=schedule_students_panel(number))


@user_router.callback_query(F.data.startswith('back_group__'))
async def back_group_panel_btn(callback: CallbackQuery):
    number = callback.data[-1]
    if number == '1':
        await first_group_btn(callback)
    elif number == '2':
        await second_group_btn(callback)


@user_router.callback_query(F.data.startswith('back_schedule__'))
async def back_schedule_panel_btn(callback: CallbackQuery):
    number = callback.data[-1]
    await callback.message.edit_text("Выберите день недели: ", reply_markup=choose_schedule_kb(number))


@user_router.callback_query(F.data == 'back__main')
async def back_main_panel_btn(callback: CallbackQuery):
    await callback.message.edit_text('<b>⚙️Панель [1TN3]: </b>', reply_markup=main_panel_kb())


@user_router.callback_query(F.data == 'lib')
async def send_lin_panel_btn(callback: CallbackQuery):
    await callback.message.edit_text('<b>Библиотека: </b>', reply_markup=library_kb())


@user_router.callback_query(F.data.startswith('book__'))
async def send_book_btn(callback: CallbackQuery):
    file_name = callback.data.split('__')[1]
    file = FSInputFile(path=books[file_name])
    await callback.message.answer_document(document=file)


@user_router.message(Command('bitcoin'))
async def get_bitcoin_course_cmd(message: Message):
    wait_message = await message.answer('Wait...')
    result = f'<b>💵{await get_bitcoin_course()}</b>'
    await wait_message.edit_text(result)


@user_router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer('/start - открыть панель\n/help - получить помощь\n/admin - открыть панель администратора')
