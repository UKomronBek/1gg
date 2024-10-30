from aiogram import Bot


async def notify_admins(admin_ids: list, bot: Bot) -> None:
    for admin_id in admin_ids:
        await bot.send_message(
            chat_id=admin_id,
            text='Hi Administrator, the Bot started successfully!'
        )
