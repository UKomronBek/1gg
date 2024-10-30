import asyncio
import logging

from aiogram.client.default import DefaultBotProperties
from colorama import Fore, init
import asyncpg

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN, DATABASE_CONFIG, ADMINS
from filters.admin_filter import AdminFilter
from handlers.admin.admin_router import admin_router
from handlers.user.user_router import user_router
from services.admin_services.notify import notify_admins
from services.bot_services.set_cmd import set_commands
from middlewares.db import DatabaseMiddleware

init(autoreset=True)
logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    print(Fore.GREEN + 'STATUS:', Fore.BLUE + "Starting bot")

    storage = MemoryStorage()

    # pool = await asyncpg.create_pool(
    #     user=DATABASE_CONFIG['user'],
    #     password=DATABASE_CONFIG['password'],
    #     database=DATABASE_CONFIG['database'],
    #     host=DATABASE_CONFIG['host']
    # )
    default_properties = DefaultBotProperties(parse_mode='html', link_preview_is_disabled=True)
    bot = Bot(token=TOKEN, default=default_properties)
    dp = Dispatcher(storage=storage)

    dp.include_router(user_router)
    dp.include_router(admin_router)

    # dp.update.middleware(DatabaseMiddleware(pool))
    admin_router.message.filter(AdminFilter())
    await set_commands(bot, ADMINS)
    try:
        await notify_admins(ADMINS, bot)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        # await pool.close()
        await bot.session.close()
def cli():
    """Wrapper for command line"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

if __name__ == '__main__':
    cli()
