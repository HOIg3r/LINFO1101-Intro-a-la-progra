def extract(code):
    string = ""
    for element in code:
        if element.isdigit():
            string += "number "
        else:
            if element.isupper():
                if element in ["A","E","I","O","U","Y"]:
                    string += "vowel-up "
                else:
                    string += "consonant-up "
            else:
                if element in ["a","e","i","o","u","y"]:
                    string += "vowel-low "
                else:
                    string += "consonant-low "
    return string