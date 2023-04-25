class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur


    def perimetre(self):
        print((self.get_longueur()+self.get_largeur())*2)

    def surface(self):
        print(self.get_longueur()*self.__largeur)

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def volume(self):
        print(self.get_longueur()*self.get_largeur()*self.get_hauteur())



rectangle = Rectangle(10, 5)
parallelepipede = Parallelepipede(10, 5, 5)
rectangle.perimetre()
rectangle.surface()
parallelepipede.volume()
