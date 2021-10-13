import json
chemistry=[]
rus=[]
algebra=[]
b=0



with open("last_res.json", "r", encoding="utf-8") as data:
    marks=json.load(data)



for i in range(len(marks["data"]["items"])):
    if marks["data"]["items"][i]["subject_name"] == "Химия":
        if marks["data"]["items"][i]["estimate_value_name"].isdigit():
            chemistry.append(marks["data"]["items"][i]["estimate_value_name"])


for i in range(len(marks["data"]["items"])):
    if marks["data"]["items"][i]["subject_name"] == "Русский язык":
        if marks["data"]["items"][i]["estimate_value_name"].isdigit():
            rus.append(marks["data"]["items"][i]["estimate_value_name"])


for i in range(len(marks["data"]["items"])):
    if marks["data"]["items"][i]["subject_name"] == "Алгебра":
        if marks["data"]["items"][i]["estimate_value_name"].isdigit():
            algebra.append(marks["data"]["items"][i]["estimate_value_name"])


with open("result.txt", "w") as result:
    result.write("Chemistry "+str(chemistry)+"\n")
    result.write("Rus "+str(rus)+"\n")
    result.write("Algebra "+str(algebra)+"\n")


