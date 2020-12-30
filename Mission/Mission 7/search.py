#code réalisé par Jacques HOGGE et Cindie Scheuren
#4 novembre 2020

#definition des fonctions

def readfile(filename): #fonctionne
    """retourne une liste des lignes dans le fichier

    la fonction retourne une liste des lignes du fichier filename avec tous les carcatères inclus

    Args:
         filename: nom du fichier
    Returns:
            une liste avec les lignes du fichier
    """
    try:
        v = []
        l = []
        with open(filename) as file:
            for line in file:
                v.append(line.rstrip())
            for words in v:
                l.append(words)
        return l
    except:
        print("Erreur: Nom de fichier inconnu!")

def get_words(line): #fonctionne
    """ retourne une liste des mots du fichier
        la fonction retourne une liste de tous les mots du fichier sans ponctuation et en minuscules

        Args:
             line : une chaine de caractère

        Returns:
                une liste avec tous les mots du fichier
        """
    try:
        l = []
        ponct = [",", ".", "?", "!", ":", "+", "=", ";", "/", "^", "*"]
        for words in line.rsplit():
            words = words.lower()
            new_word = ""
            for word in words:
                if word not in ponct:
                    new_word += word
            l.append(new_word)
        return l
    except:
        print("Erreur")




def create_index(filename): #fonctionne
    """ crée un index pour le fichier

    la fonction crée un index composé de dictionnaires imbriqués et compte le nombre d'occurrences du mot dans chaque ligne

    Args:
        filename: un nom d'un fichier .txt

    Returns:
        un index comptant les mots du fichier filename
    """
    try:

        with open(filename) as file:
            d = {}
            count_line = -1
            ponct = [",",".","?","!",":","+","=",";","/","^","*"]
            for line in file.readlines():
                count_line += 1
                words = line.strip().split()
                for word in words:
                    new_word = ""
                    for i in word:
                        if i not in ponct:
                            new_word += i.lower()
                    l = {count_line : 1}
                    if word not in d:
                        d[new_word] = l
                    else:
                        try:
                            d[new_word][count_line] += 1
                        except:
                            d[new_word][count_line] = 1
        return d
    except:
        print("Erreur: Fichier inconnu")


def get_lines(words,index): #fonctionne
    """ retourne le numéros des lignes pour les mots choisi

     retourne les identifiants des lignes qui contiennent tous les mots spécifiés dans la liste words, en utilisant le dictionnaire contenant l'index index

    Args:
        words: une liste de mots
        index: nom d'un fichier .txt


    Returns:
         le numéros des lignes pour les mots choisi
    """

    try:
        index_bis = create_index(index)
        l = []
        for i in words:
            d = []
            if i in index_bis.keys():
                for r in index_bis[i].keys():
                    if r not in d:
                        d.append(r)
                    else:
                        continue
                l.append(d)
            else:
                print("le mot " + i + " n'est pas dans le fichier")
        return l
    except:
        return


#boucle infinie pour demander le nom du fichier et la liste de mots


power = "ON"
while power != "OFF":
    l=[]
    filename = input("Veuillez entrer le nom de votre fichier: ")
    while filename == "":
        filename = input("Veuillez entrer le nom de votre fichier: ")
    lst = input("Veuillez entrer une liste de mot: ")
    while lst == "":
        lst = [input("Veuillez entrer une liste de mot: ")]
    print(get_lines(get_words(lst),filename))