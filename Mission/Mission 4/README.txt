MISSION 4

Réalisé par Jacques HOGGE et Cindie SCHEUREN
Octobre 2020

Le but de la mission 4 est de développer quelques fonctions qui permettent de traiter
des séquences d'ADN.

La première fonction que nous avons développée est la fonction is_adn() qui permet de vérifier
si une chaine de caractère est une chaine d'ADN (c'est a dire composé des caractères "a,c,g,t")

La deuxieme fonction que nous avons développée est la fonction positions(s,p) qui retourne les positions 
des occurrences de p dans s.
Nous avons eu du mal à travailler sur cette fonction car nous avons eu du mal a visualiser les index des
chaines de caractère

La troisième fonction que nous avons développée est la fonction distance_h(text1,text2) qui permet de 
calculer la distance de Hamming entre 2 chaines de caractères de longueurs égales, elle est égale au nombre
de positions ou les deux chaines sont différentes

La quatrième fonction que nous avons développée est la fonction distances_matrice(l) qui permet de calculer
une matrice de distance de Hamming entre toutes les chaines de caractères.
Cette fonction utilise la fonction distance_h() développée juste avant