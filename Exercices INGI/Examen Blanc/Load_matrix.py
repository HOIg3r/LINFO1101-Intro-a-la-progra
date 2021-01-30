file = open(filename,"r")
nb_colonne = int(file.readline())
nb_ligne = int(file.readline())
matrice = []

#création de la matrice vide
for i in range(nb_ligne):
    matrice.append([])
    for x in range(nb_colonne):
        matrice[i].append([0.0])

#emplissage  de la matrice
for line in file:
    ligne = line.split()
    n_ligne = line[0].split(",")[0]
    n_colonne = line[0].split(",")[0]
    print(n_ligne)