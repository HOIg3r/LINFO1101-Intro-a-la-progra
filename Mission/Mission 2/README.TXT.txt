MISSION 2

Réalisé par Jacques HOGGE et Cindie SCHEUREN
Date : 29 septembre 2020

L'algorithme de la MISSION 2 est un algorithme qui permet de trouver les racines entières 
d'une équation diophantienne (x^a + y^b = z^c).

Pour ce faire, nous créons la variable "solutions" qui va stocker dans sa mémoire le nombre total de solutions qu'il y a.
Ensuite, nous donnons une valeur à chaque variable en utilisant la fonction "input", qui permet de rentrer une valeur à partir de la console,
elle est associée à une fonction "int" qui permet de remplacer n'importe quelle valeur en nombre réel sans virgule.
	a = un exposant choisi
	b = un exposant choisi
	c = un exposant choisi

Par la suite, nous donnons une valeur à la variable "max" qui nous sera utile afin déterminer la limite maximale de x, y et z. Si nous ne mettions pas de limite maximale le programme ne s'arrêterait jamais.
La valeur est donnée par la fonction "input" associée à la fonction "int".

Après cela, nous créons une boucle "for" pour le x qui commence à 1 et se termine par le "max" dans cette même fonction. Il y a une boucle "for"
pour le y qui commence de 1 jusqu'au "max" et dans cette boucle il y a une dernière boucle "for" pour le z qui commence de 1 jusqu'au "max".
S'il y a 3 boucles "for" les une dans les autres c'est pour que le programme puisse essayer toutes les possibilités pour x, y et z.

Dans la dernière boucle "for" on crée une condition qui lorsque "x^a + y^b = z^c", le programme écrit la réponse dans la console et ajoute également une unité à la valeur "solutions"

une fois toutes les possibilités exécutées, le programme écrit dans la console le nombre de solutions trouvées.

Tests effectués:

x^7 + y^3 = z^2   max = 500
	x = 1 	 y = 2 	 z= 3
	x = 2 	 y = 17  z= 71
	x = 3 	 y = 9 	 z= 54
	3 solutions trouvées

x^5 + y^4 = z^2   max = 500

	x = 3 	 y = 3 	 z= 18
	x = 3 	 y = 11  z= 122
	x = 8 	 y = 8 	 z= 192
	x = 9 	 y = 18  z= 405
	4 solutions trouvées

x^3 + y^2 = z^7   max = 500

	x = 4 	 y = 8 	 z= 2
	x = 25 	 y = 250 z= 5
	2 solutions trouvées