#Programme réalisé par Jacques HOGGE et Cindie Scheuren
#Octobre 2020

import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")      # tracé rapide
turtle.bgcolor("grey")

#3
def square(size, color):     #definition de la fonction square
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()
 
#4 
def rectangle(width, height, color): #définition de la fonction rectangle
    """Trace un rectangle plein de taille `width` et height et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du rectangle.
    post: Le rectangle a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

#5
def belgian_flag(width):   #définition de la fonction belgian_flag
    """Trace un drapeau a bande Belge plein de taille `width`.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est orienté de la meme facon que au départ mais est a droite et en haut du drapeau.
    """
    rectangle(width/3, (2/3)*width, "black")
    tortue.forward(width/3)
    rectangle(width/3, (2/3)*width, "yellow")
    tortue.forward(width/3)
    rectangle(width/3, (2/3)*width, "red")
    tortue.forward(width/3)

#6
def three_color_vertical_flag(width ,color1 ,color2 ,color3): #definition de la fonction three_color_vertical_flag
    """Trace un drapeau a bande verticale plein de taille `width` et de couleur `color1,color2,color3`.

    pre: `color1,color2,color3` spécifie les 3 couleur du drapeau.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    rectangle(width/3, 2/3*(width), color1)
    tortue.forward(width/3)
    rectangle(width/3, 2/3*(width), color2)
    tortue.forward(width/3)
    rectangle(width/3, 2/3*(width), color3)
    tortue.forward(width/3)
    
def three_color_horizontal_flag(width, color1, color2, color3):
    """Trace un drapeau a bande horizontale plein de taille `width` et de couleur `color1,color2,color3`.

    pre: `color1,color2,color3` spécifie les 3 couleur du drapeau.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    rectangle(width, 2/3*(width*1/3), color1)
    tortue.right(90)
    tortue.forward(2/3*(width*1/3))
    tortue.left(90)
    rectangle(width, 2/3*(width*1/3), color2)
    tortue.right(90)
    tortue.forward(2/3*(width*1/3))
    tortue.left(90)
    rectangle(width, 2/3*(width*1/3), color3)
    tortue.right(90)
    tortue.forward(2/3*(width*1/3))
    tortue.left(90)
#7
def stars (width,color):
    """Trace une étoile pleine de taille `width` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté de l'etoile.
    post: l'etoile a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(1,6):
        tortue.forward(width)
        tortue.right(144)
    tortue.end_fill()
    tortue.penup()

#code qui crée le drapeau Européen
def european_flag(width):
    """Trace un drapeau européen de taille `width`.

    pre: `whidth` spécifie la longueur du drapeau.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.penup()
    tortue.backward(200)
    tortue.left(90)
    tortue.forward(200)
    tortue.right(90)
    tortue.pendown()
    rectangle(width,(2/3)*width, "#003399")
    tortue.forward((1/2)*width)
    tortue.right(90)
    tortue.forward((1/3)*width)
    tortue.left(90)
    for i in range(1,13):
        tortue.left(90)
        tortue.forward((2/3)*((1/3)*width))
        tortue.right(90)
        stars((2/9)*((1/3)*width),"yellow")
        tortue.right(90)
        tortue.forward((2/3)*((1/3)*width))
        tortue.left(120)
    tortue.left(90)
    tortue.forward((1/3)*width)
    tortue.right(90)
    tortue.backward((1/2)*width)

#8
#Code qui réalise les drapeau Européen aisin que les autre drapeau a coté
#le drapeau européen
european_flag(400)
tortue.backward(150+25)
tortue.left(90)
tortue.forward(150)
tortue.right(90)

#les 4 drapeaux au dessus du drapeau européen
three_color_horizontal_flag(150,"#AE1C28","#FFFFFF","#21468B")
tortue.left(90)
tortue.forward(100)
tortue.right(90)
tortue.forward(150+25)
three_color_horizontal_flag(150,"#000000","#DD0000","#FFCE00")
tortue.left(90)
tortue.forward(100)
tortue.right(90)
tortue.forward(150+100)
three_color_horizontal_flag(150,"#FFFFFF","#0033A0","#DA291C")
tortue.left(90)
tortue.forward(100)
tortue.right(90)
tortue.forward(150+25)
three_color_vertical_flag(150,"#0033A0","#FFFFFF","#DA291C")


#Les 4 drapeau belge en dessous du drapeau EU

tortue.backward(150*4+150)
tortue.right(90)
tortue.forward(150+((2/3)*400)+50)
tortue.left(90)
for i in range(1,3):
    belgian_flag(150)
    tortue.forward(25)
tortue.forward(75)
for i in range (1,3):
    belgian_flag(150)
    tortue.forward(25)
    
tortue.hideturtle()