class Person:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        print("Je suis", self.prenom, self.nom)

personne1 = Person("John", "Doe")
personne1.se_presenter()
personne2 = Person("Jean", "Dupond")
personne2.se_presenter()

