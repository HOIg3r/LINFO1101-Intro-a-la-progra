#Programme réalisé par Jacques HOGGE et Cindie SCHEUREN
#Octobre 2020

#1
#définir une fonction qui permet de voir s'il s'agit bien d'une séquence d'ADN
def is_adn(text):

#pre: rentrer une chaine de caractères d'ADN
#post : la fonction retourne True si la chaine de caractères est une séquence d'ADN et False sinon.

    text = text.upper()
    s = str(text)
    if s == "":
        return False
    for letter in text:
        if letter not in ["A", "C", "G", "T"]:
            return False     
    return True

#2
#definir une fonction qui donne la position d'une séquence d'ADN dans toute la bande d'ADN
def positions(text, car):

#pre : rentrer une chaine de carectères d'une séquence d'ADN ainsi qu'une chaine de caractaire de la partie de séquence d'ADN
#post : la fonction retourne la position de la partie de la séquence d'ADN qui se trouve dans la chaine de caractère text 

    text = text.upper()
    car = car.upper()
    l = []
    n = 0
    a = len(car)
    b = len(text)
    while n < b :
        if text[n:a]  == car:
            l.append(n)
        n += 1
        a += 1     
    return l
                
#3
#définir la fonction distance_h qui retourne la différence de distance entre les 2 str
def distance_h(text1, text2):

#pre : rentrer deux chaines de caractères d'ADN
#post : retourne la différence de distance entre les 2 bande d'ADN

    count = 0
    n = 0
    if len(text1) != len(text2):
        return None
    else:
        while n < len(text1):
            if text1[n].upper() == text2[n].upper():
                n +=1
            else:
                count +=1
                n += 1
        return count
            
#4
#definir la fonction distances_matrices
def distances_matrice(l):

#pre : rentrer une liste avec différentes séquences d'ADN
#post : retourne une matrice donnant la distance de hamming pour chaque séquence d'ADN

    matrice = []
    sous_matrice = []
    for i in range(len(l)):
        for j in range(len(l)):
            sous_matrice.append(distance_h(l[j],l[i]))
        matrice.append(sous_matrice)
        sous_matrice = []
    return matrice     