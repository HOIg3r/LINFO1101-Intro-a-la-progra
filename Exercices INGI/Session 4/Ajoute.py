def ajoute(l,v):
    present = False
    for element in l:
        if element == v:
            present = True
    if not present:
        l.append(v)
    return l