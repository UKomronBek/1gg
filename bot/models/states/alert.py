from aiogram.fsm.state import State, StatesGroup


class SendAlertMachine(StatesGroup):
    text = State()
