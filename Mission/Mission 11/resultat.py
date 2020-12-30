class Resultat:
    """
    Le rÃ©sultat d'un Coureur sur une course cycliste: le coureur et son temps.
    @author  Kim Mens, UCLouvain
    @version 01 DÃ©cembre 2019
    """

    def __init__(self, c, t):
        """
        CrÃ©e un nouveau d'un Coureur sur une course cycliste: le coureur et son temps.
        @pre: c est une instance de Coureur
              t est une instance de Temps
        @post: cette instance de Resultat a Ã©tÃ© initialisÃ© avec coureur c et temps t
        """
        self.__coureur = c  # le coureur
        self.__temps = t  # le temps effectuÃ©

    def coureur(self):
        """
        MÃ©thode accesseur.
        Retourne le coureur.
        @pre:  -
        @post: Le coureur de ce rÃ©sultat a Ã©tÃ© retournÃ©.
        """
        return self.__coureur

    def temps(self):
        """
        MÃ©thode accesseur.
        Retourne le temps.
        @pre:  -
        @post: Le temps de ce rÃ©sultat a Ã©tÃ© retournÃ©.
        """
        return self.__temps

    def __eq__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce rÃ©sultat est Ã©gal Ã  un autre, sur base de leur temps.
        @pre:  autre est une autre instance de la classe Resultat
        @post: Retourne True si le temps de ce rÃ©sultat (self) est Ã©gale
               au temps du rÃ©sultat autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return (self.temps() == autre.temps())

    def __ge__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce rÃ©sultat est plus grand ou Ã©gal au rÃ©sultat passÃ© en
        paramÃ¨tre, sur base de leur temps.
        @pre:  autre est une autre instance valide de la classe Resultat
        @post: Retourne True si ce temps de ce rÃ©sultat (self) est plus
               grand que ou Ã©gale au temps du rÃ©sultat autre passÃ© en
               paramÃ¨tre; retourne False sinon.
        """
        return (self.temps() >= autre.temps())

    def __lt__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce rÃ©sultat est plus petit que le rÃ©sultat passÃ© en
        paramÃ¨tre, sur base de leur temps.
        @pre:  autre est une autre instance valide de la classe Resultat
        @post: Retourne True si ce temps de ce rÃ©sultat (self) est plus
               petit que le rÃ©sultat autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return not (self.temps() >= autre.temps())

    def __str__(self):
        """
        MÃ©thode magique.
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: une reprÃ©sentation string de ce temps a Ã©tÃ© retournÃ©
               sous la forme de texte "NomCoureur: heures:minutes:secondes"
               Par exemple, "Alfred    : 05:02:10"
        """
        return "{0: <10} : {1}".format(self.coureur().nom(), self.temps())