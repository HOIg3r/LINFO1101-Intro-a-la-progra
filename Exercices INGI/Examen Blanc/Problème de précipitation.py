count = 0
nb_occurence = 0
for element in l:
    if element >= 0 and element < 9999:
        count += element
        nb_occurence += 1
    elif element >= 9999:
        nb_occurence += 0
    elif element < 0:
        nb_occurence += 1
return count/nb_occurence