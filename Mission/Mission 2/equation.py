#rechercher les racines d'une equation diophantienne(x^a + y^b = z^c)
#Réalise par Jacques HOGGE et Cindie SCHEUREN Septembre 2020

# associé une valeur au variables
solutions = 0
a = int(input("Entrez la valeur du coéfficient a : "))
b = int(input("Entrez la valeur du coéfficient b : "))
c = int(input("Entrez la valeur du coéfficient c : "))
max = int(input("Entrez la valeur maximal de x, y et c :"))

#boucle for pour essayer toutes les possiblités possible et ecrire au fur et a mesure des calculs les valeurs vraie
for x in range(1, max):
    for y in range(1, max):
        for z in range(1, max):
            if (x**a) + (y**b) == (z**c):
                print("x =", x,"\t","y =", y,"\t","z=", z)
                solutions += 1
            
#conditions qui ecrit le nombres de solution                 
if solutions == 0:
    print("Aucune solutions trouvées, veuillez reessayer avec d'autres valeurs")
else:
    print(solutions, "solutions trouvées")