def carre(n):
    carre = []
    count = 0
    for i in range(n):
        l = []
        for x in range(n):
            l.append(count)
            count += 1
        carre.append(l)
    return carre
            