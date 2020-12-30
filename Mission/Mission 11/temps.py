class Temps:
    """
    Un temps rÃ©alisÃ© par un Coureur, sous forme de trois nombres:
    heures, minutes, secondes.
    Un temps est valide si et seulement si les minutes et les
    secondes sont comprises entre 0 et 59.

    @auteur Kim Mens, UCLouvain
    @version 01 DÃ©cembre 2019
    """

    def __init__(self, h=0, m=0, s=0):
        """
        CrÃ©e un nouveau temps en h heures, m minutes et s secondes.
        @pre:  h est un entier >= 0
               m est un entier entre 0 et 59
               s est un entier entre 0 et 59
               Si aucun paramÃ¨tre n'est fourni, h, m et s seront 0.
        @post: cette instance de Temps a Ã©tÃ© initialisÃ© avec
               h heures, m minutes et s secondes
        """
        self.__heures = h  # le nombre d'heures
        self.__minutes = m  # le nombre de minutes, entre 0 et 59.
        self.__secondes = s  # le nombre de secondes, entre 0 et 59.

    def heures(self):
        """
        MÃ©thode accesseur.
        Retourne les heures.
        @pre:  -
        @post: le nombre d'heures de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__heures

    def minutes(self):
        """
        MÃ©thode accesseur.
        Retourne les minutes.
        @pre:  -
        @post: le nombre de minutes de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__minutes

    def secondes(self):
        """
        MÃ©thode accesseur.
        Retourne les secondes.
        @pre:  -
        @post: le nombre de secondes de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__secondes

    def __str__(self):
        """
        MÃ©thode magique.
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: une reprÃ©sentation string de ce temps a Ã©tÃ© retournÃ©
               sous la forme de texte "heures:minutes:secondes"
        Par exemple, "05:02:10" pour 5 heures, 2 minutes et 10 secondes.
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures,minutes,secondes)
        retourne le String dÃ©sirÃ© avec les nombres en deux chiffres en ajoutant
        les zÃ©ros nÃ©cessaires.
        """
        return '{:02}:{:02}:{:02}'.format(self.heures(), self.minutes(), self.secondes())

    def to_secondes(self):
        """
        Convertit ce temps en secondes.
        @pre:  -
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.secondes() + 60 * (self.minutes() + 60 * self.heures())

    def delta(self, autre):
        """
        MÃ©thode auxiliaire pour les mÃ©thodes magiques de comparaison comme __eq__ ou __ge__.
        Retourne la diffÃ©rence entre ce temps (self) et le temps (autre) passÃ© en paramÃ¨tre,
        en secondes (positif si ce temps-ci est plus grand).
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.to_secondes() - autre.to_secondes()

    def __eq__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce temps est Ã©gal au temps passÃ© en paramÃ¨tre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est Ã©gale au temps autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return (self.delta(autre) == 0)

    def __ge__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce temps est plus grand ou Ã©gal au temps passÃ© en paramÃ¨tre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est plus grand que ou Ã©gal au temps autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return (self.delta(autre) > 0)

    def add_secondes(self, temps_en_secondes):
        """
        Ajoute un nombre de secondes Ã  ce temps.
        Cette mÃ©thode sert comme mÃ©thode auxiliaire Ã  la mÃ©thode add(autre).
        @pre:  temps_en_secondes est un entier > 0
        @post: Un temps en secondes (temps_en_secondes, paramÃ¨tre de cette mÃ©thode)
               a Ã©tÃ© ajoutÃ© Ã  ce temps (self).
               Le temps sera normalisÃ© de maniÃ¨re Ã  ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unitÃ©s supÃ©rieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        time = self.to_secondes() + temps_en_secondes
        self.__secondes = time % 60
        self.__minutes = (time // 60) % 60
        self.__heures = (time // 3600) % 24

    def add(self, autre):
        """
        Ajoute un autre temps Ã  ce temps.
        @pre:  autre est une instance valide de Temps
        @post: Un autre temps (autre, paramÃ¨tre de cette mÃ©thode)
               a Ã©tÃ© ajoutÃ© Ã  ce temps (self).
               Le temps sera normalisÃ© de maniÃ¨re Ã  ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unitÃ©s supÃ©rieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        self.add_secondes(autre.to_secondes())