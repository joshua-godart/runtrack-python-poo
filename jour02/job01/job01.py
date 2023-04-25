class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
       if new_age is int:
           self.age = new_age

class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerenCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("j'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self):
        super().__init__()
        self.__matiereEnseignee = ""

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()
eleve.afficherAge()





