def translate(data, lan):
    trad = ""
    data = data.lower().split()
    for word in data:
        if word == data[-1]:
            if word.lower() in lan:
                trad += lan[word] 
            else:
                trad += word.lower() 
            return trad
        if word.lower() in lan:
            trad += lan[word] + " "
        else:
            trad += word.lower() + " "
    return trad