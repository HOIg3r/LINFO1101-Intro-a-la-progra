d = {}
for element in l:
    if element in d.keys():
        d[element] += 1
    else:
        d[element] = 1
        
num_key = 0
nb_occurence = 0
for key in d.keys():
    if d[key] > nb_occurence:
        num_key = d[key] 
        nb_occurence = d[key]
    
return num_key