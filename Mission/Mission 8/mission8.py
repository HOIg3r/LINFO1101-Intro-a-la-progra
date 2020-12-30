########################################################
#  #code réalisé par Jacques HOGGE et Cindie Scheuren  #
#  #11 novembre 2020                                   #
########################################################
class Duree:

    def __init__(self, h, m, s):
        """
        :param h: nombres d'heure
        :param m: nombres de minutes comprisent entre 0 et 60
        :param s: nombres de secondes comprisent entre 0 et 60
        """
        if 0 <= m < 60 and 0 <= s < 60:
            self.heure = h
            self.min = m
            self.sec = s

    def to_secondes(self):
        """
        Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        return ((int(self.heure)) * (60 ** 2)) + ((int(self.min)) * 60) + (int(self.sec))

    def delta(self, d):
        """
        Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        return str(int(self.to_secondes()) - int(d))

    def apres(self, d):
        """
        Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
        retourne False sinon.
        """
        if int(self.to_secondes()) >= int(d):
            return True
        else:
            return False

    def ajouter(self, d):
        """
        Ajoute une autre Duree d à cette instance de Duree (self).
        Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
        en reportant au besoin les valeurs hors limites sur les unités supérieures
        (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        h = int(d) // 3600
        m = int((d - (h * 3600))) // 60
        s = int(((d - (h * 3600)) - (m * 60)))
        self.heure += h
        self.min += m
        self.sec += s
        if self.sec > 60:
            self.min += 1
            self.sec -= 60
        if self.min > 60:
            self.heure += 1
            self.min -= 60

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{:02}:{:02}:{:02}".format(self.heure, self.min, self.sec)

class Chanson:
    def __init__(self, t, a, d):
        self.title = str(t)
        self.author = str(a)
        self.duration = str(d)

    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{:2} - {:2} - {:2}".format(self.title, self.author, self.duration)


class Album:
    def __init__(self):

        self.nb_chanson = 0
        self.duree = Duree(0, 0, 0)
        self.chansons = []

    def add(self, chanson):

        c = str(chanson).split(" - ")
        d = str(c[-1]).split(":")

        if self.nb_chanson < 100 and self.duree.to_secondes() + (int(Duree(int(d[0]), int(d[1]), int(d[2])).to_secondes())) < 75 * 60:
            self.nb_chanson += 1
            self.chansons.append(chanson)
            self.duree.ajouter(int(Duree(int(d[0]), int(d[1]), int(d[2])).to_secondes()))
            return True
        else:
            return False

    def __str__(self, a):
        self.album_name = a
        n = 0
        print("Album " + str(self.album_name) + " (" + str(self.nb_chanson) + " chansons, " + str(self.duree) + ")")
        for i in self.chansons:
            n += 1
            print(str(n) + ": " + str(i))
        return ""


if __name__ == "__main__":
    # GrÃ¢ce Ã  la ligne ci-dessus, le code ci-dessous ne sera exÃ©cutÃ© que si on n'exÃ©cute ce fichier directement.
    # Ceci nous permet d'Ã©viter que le code ci-dessous sera exÃ©cutÃ© lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    # A COMPLETER PAR LES ETUDIANTS
    # (mettez ici votre code pour crÃ©er les albums Ã  partir de la lecture du fichier 'music-db.txt')
        with open("music-db.txt") as file:
            n = 0
            l = []

            for line in file:
                line = line.split()
                chanson = Chanson(line[0], line[1], Duree(0, int(line[-2]), int(line[-1])))
                l.append(chanson.__str__())

            while n < len(l):
                album = Album()
                a = 1
                for music in l:
                    if int(album.nb_chanson) < 100 and int(album.duree.to_secondes()) + Duree(0, int(line[-2]), int(line[-1])).to_secondes() < 75*60:
                        album.add(music)
                    else:
                        album.__str__(a)
                        print("\n")
                        album = Album()
                        album.add(music)
                        a += 1
                album.__str__(a)
                break