from aiogram.utils.keyboard import InlineKeyboardBuilder


def send_admin_panel_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text='Отправить уведомление', callback_data='send_alert')
    builder.button(text='Шаблоны', callback_data='send_template')
    builder.adjust(2)
    return builder.as_markup()


def back_admin_panel():
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data='back_admin_panel')
    builder.adjust(1)
    return builder.as_markup()
