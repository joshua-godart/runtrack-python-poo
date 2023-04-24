class Animal:
    def __init__(self):
        self.age = int(input("entrez l'âge de l'animal : "))
        self.name = ""
        print("L'âge de l'animal a", self.age, "ans")

    def vieillir(self):
        self.age += 1
        print("L'âge de l'animal a", self.age, "ans")

    def nommer(self):
        self.name = input("entrez le nom de l'animal :")
        print("Le nom de l'animal est", self.name)

animal = Animal()
animal.vieillir()
animal.nommer()