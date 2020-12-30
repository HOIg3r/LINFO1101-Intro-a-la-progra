import unittest
from classement import Classement
from resultat import Resultat
from coureur import Coureur
from temps import Temps

class ClassementTest(unittest.TestCase):

    def setUp(self):
        self.cl = Classement()
        self.coureur1 = Coureur('Kim', 45)
        self.coureur2 = Coureur('Charles', 50)
        self.coureur3 = Coureur('Siegfried', 35)

    def test_size(self):
        self.assertEqual(self.cl.size(), 0)
        self.cl.add(Resultat(self.coureur1, Temps(0,12,33)))
        self.assertEqual(self.cl.size(), 1)
        self.cl.add(Resultat(self.coureur2, Temps(0, 12, 33)))
        self.assertEqual(self.cl.size(), 2)
        self.cl.add(Resultat(self.coureur2, Temps(0, 12, 33)))
        self.cl.add(Resultat(self.coureur2, Temps(0, 12, 33)))
        self.assertEqual(self.cl.size(), 4)

    def test_add(self):
        self.cl.add(Resultat(self.coureur1, Temps(0, 12, 33)))
        self.cl.add(Resultat(self.coureur2, Temps(1, 1, 32)))
        self.cl.add(Resultat(self.coureur3, Temps(0, 0, 0)))

    def test_remove(self):
        self.cl.add(Resultat(self.coureur1, Temps(0, 12, 33)))
        self.cl.remove(Resultat(self.coureur1, Temps(0, 12, 33)))


if __name__ == '__main__':
    unittest.main()