from aiogram.dispatcher.filters import Command, state
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from aiogram import types

from states import Form

@dp.message_handler(Command("form"))
async def enter_test(message: types.Message):
    await message.answer("Введите имя:")
    await Form.name.set()


@dp.message_handler(state=Form.name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(name=name)

    await message.answer("Введите email:")

    await Form.mail.set()


@dp.message_handler(state=Form.mail)
async def get_mail(message: types.Message, state: FSMContext):
    mail = message.text

    await state.update_data(mail=mail)

    await message.answer("Введите номер телефона:")

    await Form.number.set()


@dp.message_handler(state=Form.number)
async def get_number(message: types.Message, state: FSMContext):

    data = await state.get_data()

    number = message.text
    name = data.get("name")
    mail = data.get("mail")

    await message.answer(f"Привет {name}! Ты ввел следующие данные:")
    await message.answer(f"Имя - {name}")
    await message.answer(f"Email - {mail}")
    await message.answer(f"Номер телефона - {number}")
    await message.answer("Вся информация будет сохранена и использована против вас!!!")

    await state.finish()