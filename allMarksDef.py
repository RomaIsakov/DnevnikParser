import json
import requests
from statistics import mean
from session_from_headers import headersMiner
from dnevnik import *
from beautifulMarks import beautifuMarksMaker
def parsing():
    headersMiner()
    marksParser()
def allMarksDef(dict, key):
    chemistry=[]
    rus=[]
    algebra=[]
    geometry=[]
    IT=[]
    physics=[]
    literature=[]
    biology=[]
    geography=[]
    eng=[]
    society=[]
    OBJ=[]
#                                      ===[] - Hammer
    technology=[]
    PE=[]
    history=[]
    b=0
    codeList=["1084", "1058", "1077", "1063", "1086", "11204", "1065", "1087", "1089", "11080", "1088", "1083", "1092"]
    for i in range(len(dict["data"]["items"])):
        try:
            int(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Обществознание":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    society.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "История России. Всеобщая история":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    history.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Информатика":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    IT.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Физическая культура":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    PE.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Технология":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    technology.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Основы безопасности жизнедеятельности":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    OBJ.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Химия":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    chemistry.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Иностранный язык (английский)":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    eng.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "География":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    geography.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Биология":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    biology.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Русский язык":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    rus.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Алгебра":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    algebra.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Геометрия":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    geometry.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Литература":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    literature.append(dict["data"]["items"][i]["estimate_value_name"])
            if dict["data"]["items"][i]["subject_name"] == "Физика":
                if dict["data"]["items"][i]["estimate_type_code"] in codeList:
                    physics.append(dict["data"]["items"][i]["estimate_value_name"])
        except:
            pass
    mathDict={
            "Рус. Яз":rus,
            "Алгебра":algebra,
            "Химия":chemistry,
            "Геометрия":geometry,
            "Биология":biology,
            "География":geography,
            "Англ. Яз":eng,
            "Общество":society,
            "ОБЖ":OBJ,
            "Технология":technology,
            "Физра":PE,
            "Физика":physics,
            "История":history,
            "Информатика":IT,
            "Литра":literature
        }

#key==1-возвращает словарь mathDict, словарь типа "предмет: оценка"
#key==0-возращает красивую строку!

    if key==1:
        return(mathDict)
    elif key==0:
        res_text=""
        for key in mathDict:
            res_text+=key
            res_text+=": "
            for i in range(len(mathDict[key])):
                res_text+=str(mathDict[key][i])
                res_text+=", "
            res_text+="\n"
        return(res_text)
def jsonDumper(dict, fileName):
    with open(fileName+".json","r", encoding="utf-8")as file:
        json.dump(dict, file)
def getNewMarks():
    with open("last_res.json", encoding="utf-8") as file:
        marks=json.load(file)
    marksLen=len(marks["data"]["items"])
    print(marksLen)
    parsing()
    with open("last_res.json", encoding="utf-8") as file:
        marks1=json.load(file)
    marksLen1=len(marks1["data"]["items"])
    newMarks=marksLen1-marksLen
    newMarksDict=[]
    print(newMarks)
    for i in range(newMarks):
        newMarksDict.append(marks1["data"]["items"][i])
    return beautifuMarksMaker(newMarksDict)

def markParser():
    pass
#Средний бал по всем предметам
def allAvg():
    parsing()
    avgDict={}
    with open("last_res.json", "r", encoding="utf-8") as file:
        dict = json.load(file)
    allMarks=allMarksDef(dict, 1)#Получаем словарь со всеми предметами
    mathDictClear=[]
    for i in allMarks:#Убирает замечания
        for j in range(len(allMarks[i])):
            if allMarks[i][j]!="Замечание":
                mathDictClear.append(int(allMarks[i][j]))
        allMarks[i]=mathDictClear
        mathDictClear=[]
    for i in allMarks:
        if len(allMarks[i])!=0:
            allMarks[i]=round(mean(allMarks[i]), 2)
        else:allMarks[i]="-"
    res_text=""
    for key in allMarks:
        res_text+=key
        res_text+=": "
        res_text+=str(allMarks[key])
        res_text+="\n"
    return res_text
if __name__ == "__main__":
    allAvg()