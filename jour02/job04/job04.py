class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur
    def get_largeur(self):
        return self.largeur
    def aire(self):
        print(self.get_longueur()*self.get_largeur())

forme = Forme()
print(forme.aire())
rectangle = Rectangle(10, 5)
rectangle.aire()