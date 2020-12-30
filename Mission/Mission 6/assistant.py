#programme Mission 6
#Réalisé par Cindie SCHEUREN et Jacques HOGGE
#28 octobre 2020

print('\nBienvenue dans votre assistant personalisée !\nTaper la commande "help" pour connaitre toutes les commandes et leur fonctionnement.') #Message d'entrée du programme
commands = ["file", "info", "dictionary", "search", "sum", "avg", "help", "exit"]  # Listes de toutes les commandes
command = ""
b = 0 #variable qui permet de savoir si il est en mode dictionnaire ou pas

#Definitions de toutes les commandes du programme

def file(filename):

    """ ouvre le fichier

    La fonction ouvre le fichier et le lit afin d'y ressortir des informations

    Args:
        argument filename: Nom du fichier que on veut lire.

      Returns:
          la fonction ne retourbe rien, elle ouvre juste le fichier et enregistre le nom du fichier
    """

    try:
        a = 0
        file = open(filename, 'r')
        file.read()
    except:
        a = 1
        print("Fichier inconnue, recommencé")
    if a == 0:
        print("Loaded " + filename + "\n")


def info():

    """ Donne les infos du fichier chargé

    La fonction ecrit dans la console le nombre de ligne et de caractères que contient le fichier

    Args:
        pas d'argument
    Returns:
        ecrit dans la console le nombre de lingne et de caractères du fichier
    """

    try:
        file = open(file_name, "r")
        lines = 0
        caracts = 0
        for line in file:
            lines += 1
            caracts += len(line)
        print("Voici les informations du fichier chargé " + file_name + ".\n")
        print("\t" + str(lines) + " lines")
        print("\t" + str(caracts) + " caracters\n")

    except:
        print('Fichier non chargé, veuillez charger votre fichier avec la commande "file".\n')


def exit():

    """ Imprime un message de fermeture du porgramme
    """
    print("Fermeture du programme !\nAu plaisir de vous revoir !\nA Bientot!")


def dictionary():
    try:
        v = []
        l = []
        file = open(file_name, 'r')
        for line in file:
            v.append(line.split(','))
        for f in v:
            l.append(f[0])
        l = sorted(l)
        print("Fichier lu comme un dictionnaire a partir de maintenant.")
        return l

    except:
        print('Fichier non chargé, veuillez charger votre fichier avec la commande "file".')

def search(name):
    """ trouve si un mot est dans le fichier

    la fonction cherche dans le fichier si un mot y est présent

    Args:
        name : le nom que on recherche

    Returns:
        si le mot est présent, elle dit que il est présent
        si le mot est pas présent, elle dit que il est pas présent
    """
    if b == 1:
        l = dictionary()
        first = 0
        last = len(l)
        found = False

        while first <= last and not found:
            middle = (first + last)//2
            if l[middle] == name:
                found = True
            else:
                if name < l[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
        if found == True:
            print(name + " est dans le dictionnaire")
        else:
            print(name + " n'est pas dans le dictionnaire")
    else:
        print("Vous ne liser pas le fichier en mode dictionnaire, activer le.\n")

def sum(numbers):
    """ fait la somme des nombres

    La fonction fait la somme de tous les nombres donné

    Args:
        numbers: qui est une liste de tous les nombres a additioner entre eux

    Returns:
        la somme de tous les nombres
    """
    try:
        sum = 0
        for i in numbers:
            sum += int(i)
        print("La somme de tous les nombres est de : " + str(sum))
        return sum
    except:
        print("Erreur ! Veuillez entrer seulement des nombres pour faire la somme de ceux-ci !")


def avg(numbers):
    """ fait la moyenne des nombres.

    cette fonction fait la moyenne des nombres donnés

    Args:
        numbers: qui est une liste  de nombres

    Returns:
        la moyenne des nombres
    """
    try:
        sum = 0
        for i in numbers:
            sum += int(i)
        moy = sum//int(len(numbers))
        print("La moyenne de tous les nombres est de : " + str(moy) + " !")
        return moy
    except:
        print("Erreur ! Veullez entrer seulement des nombres pour faire la moyenne de ceux-ci !")

def help():
    """donne toutes les fonction du programme

    la fonction ecrit toutes les fonctions du programme ainsi que ce qu'elle font

    Returns:
        ecrit dans la console
    """
    print("\nVoici toutes les commandes mise a votre dispositions\n")
    print("\tFile <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment")
    print("\tInfo: montre le nombre de lignes et de caractères du fichier")
    print("\tDictionary: utilise le fichier comme dictionnaire à partir de maintenant")
    print("\tSearch <word>: détermine si le mot est dans le dictionnaire")
    print("\tSum <number1> ... <numbern>: calcule la somme des nombres spécifiés")
    print("\tAvg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés")
    print("\tHelp: montre des instructions à l'utilisateur")
    print("\tExit: arrête l'outil\n")



#boucle qui prend en input la commande et la fait fonctionner
#la boucle ne s'arrete  pas tant que on lui dit pas
continueLoop = True
while continueLoop:
    command = input("Entrez la commande souhaitée: ").lower()
    print("")
    command = command.split(" ")
    if not command[0] in commands:
        print("Commande inconnue, veuillez recommencer avec une commande valide svp.\n")

    if command[0] == "file":
        try:
            file(command[1])
            file_name = command[1]
        except:
            print("Veulliez donner le nom de votre fichier en meme temp que la commande 'file'.\n")

    if command[0] == "info":
        info()
    if command[0] == "exit":
        exit()
        continueLoop = False
    if command[0] == "dictionary":
        b = 1
        dictionary()
    if command[0] == "search":
        search(command[1])
    if command[0] == "sum":
        sum(command[1:])
    if command[0] == "avg":
        avg(command[1:])
    if command[0] == "help":
        help()
