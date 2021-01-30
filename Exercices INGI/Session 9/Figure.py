class Figure:

    def __init__(self,x,y,visible=False) :
        """
        @pre x, y sont des entiers représentant des positions sur l'écran
        @post Une figure a été créée avec centre de gravité aux coordonnées x,y.
              Cette figure n'est initialement pas visible
        """
        self.__x = x
        self.__y = y
        self.__visible = visible
        
    def get_x(self):
        return self.__x
      
    def get_y(self):
        return self.__y

    def estVisible(self) :
        """
        @pre -
        @post a retourné la visibilité de cette figure
        """
        return self.__visible

    def surface(self):
        """
        @pre -
        @post la surface (un float) de la figure a été calculé et retournée
        """
        pass            # code non fourni

class Rectangle(Figure):

    def __init__(self,lo,la,x,y) :
        """
        @pre lo (longeur) et la (largeur) sont des entiers positifs
             x, y sont des entiers représentant des positions sur l'écran
        @post un rectangle dont le centre de gravite est en x,y
              et ayant comme longueur lo et comme largeur la a été créé
        """
        super().__init__(x,y)
        self.longeur = lo
        self.largeur = la
        
    def surface(self):
        """
        @pre -
        @post la surface (un float) du rectangle a été calculé et retournée
        """
        return self.longueur*self.largeur
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
      
    def __equal__(self, other):
        return self.surface() == other.surface()

    def __str__(self) :
        return str((self.longeur,self.largeur,self.get_x(),self.get_y(),self.estVisible()))
