class Coureur:
    """
    ReprÃ©sente un coureur cycliste.
    @author  Kim Mens, UCLouvain
    @version 01 DÃ©cembre 2019
    """

    def __init__(self, nom, age):
        """
        @pre: nom est un string non-vide
              age est un entier > 0
        @post: un coureur nommÃ© nom et Ã¢gÃ© age a Ã©tÃ© crÃ©Ã©
        """
        self.__nom = nom  # Le nom du coureur
        self.__age = age  # L'age du coureur.

    def nom(self):
        """
        MÃ©thode accesseur
        @pre:  -
        @post: le nom du coureur a Ã©tÃ© retournÃ©
        """
        return self.__nom

    def age(self):
        """
        MÃ©thode accesseur
        @pre:  -
        @post: l'Ã¢ge du coureur a Ã©tÃ© retournÃ©
        """
        return self.__age

    def __eq__(self, other):
        """
        MÃ©thode magique
        Teste si ce coureur est Ã©gal a un objet quelconque.
        Le critÃ¨re d'Ã©galitÃ© porte sur le nom et l'Ã¢ge du coureur.
        @pre:  -
        @post: Retourne True si other est egal Ã  self (meme type et valeurs des attributs);
               retourne False sinon.
        """
        return (type(other) == Coureur) and (self.nom() == other.nom()) and (self.age() == other.age())

    def __hash__(self):
        """
        MÃ©thode magique
        Retourne un hash code pour cet objet. Ceci est nÃ©cessaire pour utiliser un objet de type
        Coureur comme clÃ© d'une dictionnaire, comme dans notre implÃ©mentation naÃ¯ve du classement.
        Remarque: Pour votre implÃ©mentation vous pouvez ignorer cette mÃ©thode; elle n'est pas importante
                  si on stocke les rÃ©sultats dans une liste chaÃ®nÃ©e plutÃ´t que dans une dictionnaire.
        """
        return hash(str(self))

    def __str__(self):
        """
        MÃ©thode magique
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: Retourne un reprÃ©sentation avec le nom et l'Ã¢ge de ce coureur,
               dans le format "Coureur NOM (age AGE)"
        """
        return "Coureur " + self.nom() + " (Ã¢ge " + str(self.age()) + ")"