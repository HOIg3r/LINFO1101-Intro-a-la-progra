def create_dictionary(filename):
    with open(filename,) as file:
        l = []
        d = {}
        for line in file.readlines():
            line = line.strip().split()
            for word in line:
                l.append(word)
                
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
            
    return d

def occ(dictionary, word):
    try:
        return dictionary[word]
    except KeyError:
        return 0
        
            
        