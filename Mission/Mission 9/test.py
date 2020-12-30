#Réalisé par Jacques HOGGE et Cindie SCHEUREN
#18 novembre 2020
"""
    Tests fournis pour la mission 9; Ã  complÃ©ter par les Ã©tudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

from mission9 import *

"""
   Classe de test initiale pour la classe Article.
   @author Kim Mens
   @version 18 novembre 2018
"""


class TestArticleInitial:
    articles = [Article("laptop 15\" 8GB RAM", 743.79),
                Article("installation windows", 66.11),
                Article("installation wifi", 45.22),
                Article("carte graphique", 119.49),
                ArticlePiece(1, Piece("disque dur 350 GB", 49.99, 0.355, True), "disque dur 350 GB", 49.99),
                ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.176), 'souris bluetooth', 15.99),
                ArticleReparation("Souris", 0.75),
                ArticlePiece(5, Piece("adaptateur DVI - VGA", 12), 'adaptateur DVI - VGA', 12),
                ArticlePiece(2, Piece("Java in a Nutshell", 24, 0.321, False, True), "Java in a Nutshell", 24),
                ArticlePiece(5, Piece("souris bluetooth", 15.99, 0.176), 'souris bluetooth', 15.99)]



    @classmethod
    def run(cls):
        for art in cls.articles:
            print(art)


"""
   Classe de test initiale pour la classe Facture.
   @author Kim Mens
   @version 8 novembre 2020
"""


class TestFactureInitial:
    facture = Facture(1, "PC Store - 22 novembre", TestArticleInitial.articles)

    @classmethod
    def run(cls):
        print(cls.facture)


facture_livraison = Facture(1, "PC Store - 22 novembre", TestArticleInitial.articles)

if __name__ == "__main__":
    print("*** TEST DE LA CLASSE Article ***")
    print()
    TestArticleInitial.run()

    print()
    print("*** TEST DE LA CLASSE Facture ***")
    print()
    TestFactureInitial.run()

    print("*** TEST DE LA CLASSE Facture en livraison ***")
    print()
    a = Facture(1, 'PC store 22 octobre', TestArticleInitial().articles)
    print(a.printLivraison())



