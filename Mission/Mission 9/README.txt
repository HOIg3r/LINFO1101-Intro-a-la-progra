Mission par Jacques HOGGE et Cindie Scheuren
18 Novembre  2020
Pour cette mission, nous devions creer un programme informatique qui permet de creer des factures.
Pour cela, nous avons creer plusieurs classe, Une classe Article qui permet de creer un article sur base de ça description
et de sont prix. Il y a d'autre fonction permetant de connaitre le prix hors TVA, le taux de TVA ...
La classe possède aussi une fonction qui permet d'imprimer la description de l'article ainsi que le prix

Ensuite il y a une Classe ArticleReparation qui est un classe fille de la classe article, elle a les meme caractéristique
en plus du temps qui va etre nécèssaire a la réparation de l'article a défaut de 20 euros plus 35h de l'heure

Ensuite, il y a une Classe Piece qui permet de creer un Piece avec comme caractéristique, la description, le prix,
le poids, si il s'agit d'une piece fragile, et si il s'agit d'une piece a Tva réduite
Plusieur fonction permet  de retourner la valeur de ces caractéristiques

Ensuite il y a une Classe ArticlePiece qui est une classe fille de la classe Article. Elle a les meme caractéristique en
plus de du nombre de piece et la Piece. Des fonctions permettent de retourner les valeur des caractéristiques

Ensuite il y a une Classe Facture qui permet d'imprimer une facture bien structurée, Nous avons ajouter un fonction
PrintLivraison qui permet d'imprimer un facture seulement pour les piece qui doivent etre livrée et qui indique leurs nombres
leur poids et si elles sont fragiles

Nous n'avons pas rencontré de probleme durant la l'ecriture du Code

Pour faire le Test, il suffit juste de lancer le fichier test.py