#donner une valeur a chaque variables
n = 1
a = 1
b = 1
c = 1

#faire un boucle pour calculer les 10 premiers nombre, les nombres au carré et la sommes des nombres au carrés
while a != 11:
    print(a, "\t", b, "\t", c, "\t", n*(n+1)*(2*n+1)//6)
    n = n+1
    a = a+1
    b = a**2
    c = c + b
    