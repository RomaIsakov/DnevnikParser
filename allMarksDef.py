import json
from session_from_headers import headersMiner
from dnevnik import *
def parsing():
    headersMiner()
    marksParser()
def allMarksDef(dict):
    parsing()
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
    technology=[]
    PE=[]
    b=0

    for i in range(len(dict["data"]["items"])):
        if dict["data"]["items"][i]["subject_name"] == "Обществознание":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                society.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Физическая культура":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                PE.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Технология":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                technology.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Основы безопасной жизнедеятельности":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                OBJ.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Химия":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                chemistry.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Иностранный язык ":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                eng.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "География":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                geography.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Биология":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                biology.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Русский язык":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                rus.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Алгебра":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                algebra.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Геометрия":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                geometry.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Физика":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                physics.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Информатика":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                IT.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Литература":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                literature.append(dict["data"]["items"][i]["estimate_value_name"])
        if dict["data"]["items"][i]["subject_name"] == "Физика":
            if dict["data"]["items"][i]["estimate_type_code"]=="1058":
                physics.append(dict["data"]["items"][i]["estimate_value_name"])

        mathDict={
            "Русский язык":rus,
            "Алгебра":algebra,
            "Химия":chemistry,
            "Геометрия":geometry,
            "Биология":biology,
            "География":geography,
            "Иностранный язык":eng,
            "Обществознание":society,
            "Основы безопасной жизнедеятельности":OBJ,
            "Технология":technology,
            "Физическая культура":PE,
            "Физика":physics
        }
        return(mathDict)
def jsonDumper(dict, fileName):
    with open(fileName+".json","r", encoding="utf-8")as file:
        json.dump(dict, file)
def getNewMarks():
    with open("last_res.json", encoding="utf-8") as file:
        marks=json.load(file)
    marksLen=len(marks)
    parsing()
    with open("last_res.json", encoding="utf-8") as file:
        marks1=json.load(file)
    marksLen1=len(marks1)
    newMarks=marksLen1-marksLen
    print(newMarks)
    count=0
    newMarksDict={}
    for i in marks:
        newMarksDict[i]=marks[i]
        count+=1
        if count==newMarks:
            break
    newMarksDict=allMarksDef(newMarksDict)
    print(newMarks)
    return newMarksDict

def markParser():
    pass