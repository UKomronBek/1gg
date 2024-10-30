from aiogram import Router, Bot, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.config import FIRST_GROUP_ADMIN, SECOND_GROUP_ADMIN, \
    first_schedule_templates, second_schedule_templates, FIRST_GROUP_STUDENTS, SECOND_GROUP_STUDENTS, \
    AVAILABLE_CONTENT_TYPES
from bot.keyboards.inline.admin_panel_kb import send_admin_panel_kb, back_admin_panel
from bot.models.states.alert import SendAlertMachine

admin_router = Router(name='admin_router')


@admin_router.message(Command('admin'))
async def send_admin_panel(message: Message):
    await message.answer("Админ панель: ", reply_markup=send_admin_panel_kb())


@admin_router.callback_query(F.data == 'send_alert')
async def send_alert_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('<b>Введите текст: </b>')
    await state.set_state(SendAlertMachine.text)


@admin_router.message(SendAlertMachine.text)
async def input_alert_cmd(message: Message, bot: Bot):
    text = message.text
    uid = message.from_user.id
    if uid in FIRST_GROUP_ADMIN and uid in SECOND_GROUP_ADMIN:
        students = FIRST_GROUP_STUDENTS.append(SECOND_GROUP_STUDENTS)
        which_group = "1, 2"
    else:
        students = FIRST_GROUP_STUDENTS if uid in FIRST_GROUP_ADMIN else SECOND_GROUP_STUDENTS
        which_group = '1' if uid in FIRST_GROUP_ADMIN else '2'

    print(message.content_type.value)
    print(type(message.content_type))

    if message.content_type in AVAILABLE_CONTENT_TYPES:
        for student in students:
            try:
                await bot.copy_message(student, message.from_user.id, message.message_id)
            except TelegramBadRequest:
                pass

        await message.answer(f'Уведомления отправлены группе - {which_group}!')


@admin_router.callback_query(F.data == 'send_template')
async def send_template_cmd(callback: CallbackQuery):
    if callback.from_user.id in FIRST_GROUP_ADMIN:
        result = '\n'.join(first_schedule_templates)
        await callback.message.edit_text(result, reply_markup=back_admin_panel())
    elif callback.from_user.id in SECOND_GROUP_ADMIN:
        result = '\n'.join(second_schedule_templates)
        await callback.message.edit_text(result, reply_markup=back_admin_panel())


@admin_router.callback_query(F.data == 'back_admin_panel')
async def back_admin_panel_btn(callback: CallbackQuery):
    await callback.message.edit_text("Админ панель: ", reply_markup=send_admin_panel_kb())
