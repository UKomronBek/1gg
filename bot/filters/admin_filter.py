from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.config import ADMINS


class AdminFilter(BaseFilter):
    async def __call__(self, event: Message):
        uid = event.from_user.id
        if uid in ADMINS:
            return True
        await event.answer('Нет прав!')
