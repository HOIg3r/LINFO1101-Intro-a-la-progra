def translate(data):
    reponse = ""
    for letter in data:
        if letter.upper() in morse.keys():
                reponse += morse[letter.upper()]
                
        else:
            raise TypeError
    return reponse       