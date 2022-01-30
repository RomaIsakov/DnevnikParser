def beautifuMarksMaker(marksList):
    result=""
    for i in range(marksList):
        mark=marksList[i]["estimate_value_name"]
        subject=marksList[i]["subject_name"]
        result+=subject+": "+mark+"\n"
    return result
