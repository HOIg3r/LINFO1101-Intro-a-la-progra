if list == []:
    return None
else:
    count = 0
    nb = 0
    for element in list:
        count += element
        nb += 1
    return count/nb
        