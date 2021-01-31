from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    mail = State()
    number = State()