from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.config import books, books_trivial, week_days


def main_panel_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="IHT Web-site🌐", url="https://iht.uz")
    builder.button(text="1-подгруппа", callback_data="first_group")
    builder.button(text="2-подгруппа", callback_data="second_group")
    builder.button(text="Библиотека📚", callback_data="lib")
    # builder.button(text="Список учеников👨‍🎓👩‍🎓", callback_data="students_list")
    builder.adjust(1, 2, 1, 1)
    return builder.as_markup()


def group_panel_kb(number: int):
    builder = InlineKeyboardBuilder()
    builder.button(text='Расписание🗓️', callback_data=f'group_schedule__{number}')
    builder.button(text='Список учеников👨‍🎓👩‍🎓', callback_data=f'group_students__{number}')
    builder.button(text='🔙 Назад', callback_data='back__main')
    builder.adjust(2, 1)
    return builder.as_markup()


def schedule_students_panel(number: int):
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data=f'back_group__{number}')
    builder.adjust(1)
    return builder.as_markup()


def choose_schedule_kb(number: int):
    builder = InlineKeyboardBuilder()
    for day, trivial in week_days.items():
        builder.button(text=trivial, callback_data=f'scheduleday_{day}_{number}')
    builder.button(text='🔙 Назад', callback_data=f'back_group__{number}')
    builder.adjust(2)
    return builder.as_markup()


def back_scheduler_panel(number: int):
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data=f'back_schedule__{number}')
    builder.adjust(1)
    return builder.as_markup()


def library_kb():
    builder = InlineKeyboardBuilder()
    for name in books:
        builder.button(text=books_trivial[name], callback_data=f'book__{name}')
    builder.button(text='🔙 Назад', callback_data='back__main')
    builder.adjust(2, 2, 2, 2, 2, 1)
    return builder.as_markup()
