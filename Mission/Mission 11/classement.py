from orderedlinkedlist import Orderedlinkedlist

class Classement :
    """
    Une implÃ©mentation primitive de classement, non ordonnÃ©e et de capacitÃ© fixe.
    @author Kim Mens
    @version 01 DÃ©cembre 2019
    """

    __maxcapacity = 10

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a Ã©tÃ© crÃ©Ã©
        """
        self.__resultats = Orderedlinkedlist()
        self.__size = 0         # nombre de rÃ©sultats actuel (initialement 0, maximum __maxcapacity)

    def size(self):
        """
        MÃ©thode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de rÃ©sultats actuellement stockÃ©s dans ce classement a Ã©tÃ© retournÃ©.
        """
        return self.__size

    def add(self,r):
        """
        Ajoute un rÃ©sultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le rÃ©sultat r a Ã©tÃ© insÃ©rÃ© selon l'ordre du classement.
               En cas d'ex-aequo, r est insÃ©rÃ© aprÃ¨s les autres rÃ©sultats de mÃªme ordre.
        ATTENTION : L'implÃ©mentation actuelle ne respecte pas encore la post-condition!
                    Le rÃ©sultat est simplement ajoutÃ© Ã  la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des Ã©lÃ©ments.
        """
        if self.size() >= self.__maxcapacity :
            raise Error("Capacity of classement exceeded")
        else :
            self.__size += 1
            self.__resultats.add(r)

    def get(self,c):
        """
        Retourne le rÃ©sultat d'un coureur donnÃ©.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return self.__resultats.get(c)

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post e pas dans le classement.
        ATTENTION : L'implÃ©mentation actuelle ne respecte pas encore la post-condition!
                    Etant donnÃ© que la dictionnaire de rÃ©sultats ne connaÃ®t pas de position,
                    pour le moment cette mÃ©thode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaÃ®nÃ©e ordonnÃ©e
                    comme structure de donnÃ©es, plutÃ´t qu'une simple dictionnaire.
        """
        return self.__resultats.get_position(c)

    def remove(self,c):
        """
        Retire un rÃ©sultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) rÃ©sultat pour le coureur c du classement.
              c est comparÃ© au sens de __eq__. Retourne c si un rÃ©sultat a Ã©tÃ© retirÃ©,
              of False si c n'est pas trouvÃ© dans la liste.
        """
        self.__size -= 1
        return self.__resultats.pop(c)

    def __str__(self):
        """
        MÃ©thode magique
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: Retourne une reprÃ©sentation de ce classement sous forme d'un string,
               avec une ligne par rÃ©sultat.
        """
        s = ""
        result = self.__resultats.lst()
        for line in result:
            s += "{0: <10} : {1}\n".format(line.coureur().nom(),line.temps())
        return s