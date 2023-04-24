class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5

    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur

    def set_valeur(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur


rectangle = Rectangle()
print("les longueur et largeur du rectangle sont de", rectangle.get_longueur(), "et", rectangle.get_largeur())
rectangle.set_valeur(20, 10)
print("les nouvelles longueur et largeur du rectangle sont de", rectangle.get_longueur(), "et", rectangle.get_largeur())