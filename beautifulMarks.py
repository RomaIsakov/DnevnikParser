def beautifuMarksMaker(marksList):
    result=""
    if len(marksList)!=0:
        for i in range(marksList):
            mark=marksList[i]["estimate_value_name"]
            subject=marksList[i]["subject_name"]
            result+=subject+": "+mark+"\n"
        return result
    else:
        return "Нет новых оценок"
