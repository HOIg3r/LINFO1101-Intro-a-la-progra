def recherche(m,v):
    check = False
    for ligne in m:
        if v in ligne:
            check = True
    return check