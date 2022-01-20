from aiogram import Bot,Dispatcher,executor,types
from config import token, userId
import json
from aiogram.dispatcher.filters import Text
from allMarksDef import *
bot=Bot(token)
dp=Dispatcher(bot)
with open("last_res.json", "r", encoding="utf-8") as file:
    dict=json.load(file)
count = 0

@dp.message_handler(commands="start")
async def start(message:types.message):
    buttonsNames=["Все оценки", "Средний балл", "Новые оценки"]
    keyBoard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyBoard.add(*buttonsNames)
    await message.answer("Я бот, здравствуйте", reply_markup=keyBoard)
@dp.message_handler(Text(equals="Все оценки"))
async def allMarks(message:types.message):
    #global count
    message_count = 0
    print(dict)
    result = allMarksDef(dict, 0)
    await message.answer(result)

@dp.message_handler(Text(equals="Новые оценки"))
async def regress(message: types.message):
    result=getNewMarks()
    for markNumber in result:
        subjectName=markNumber
        mark=list(map(int,result[markNumber]))
        if len(mark)==0:
            avg=0
        else:
            avg=round(sum(mark)/len(mark), 2)
        res=f"{subjectName}:\nОценки: {mark}\nСредний балл: {avg}"
        await message.answer(res)


@dp.message_handler(Text(equals="Средний балл"))
async def avg(message: types.message):
    await message.answer(allAvg())
if __name__ == "__main__":
    executor.start_polling(dp)
