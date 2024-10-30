from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat


async def set_user_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command='/start', description='Открыть панель.'),
        BotCommand(command='/help', description='Получить помощь.'),
    ]
    scope = BotCommandScopeDefault(type='default')
    await bot.set_my_commands(commands=commands, scope=scope)


async def set_admin_commands(bot: Bot, admin_ids: list) -> None:
    commands = [
        BotCommand(command='/admin', description='Открыть панель администратора'),
        BotCommand(command='/start', description='Открыть панель.'),
        BotCommand(command='/help', description='Получить помощь.'),
    ]
    for admin_id in admin_ids:
        scope = BotCommandScopeChat(type='chat', chat_id=admin_id)
        await bot.set_my_commands(commands=commands, scope=scope)


async def set_commands(bot: Bot, admin_id: str) -> None:
    await set_user_commands(bot)
    await set_admin_commands(bot, admin_id)
