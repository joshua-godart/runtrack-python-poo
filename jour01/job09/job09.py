class Student:
    def __init__(self, prenom, nom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credit = 0

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero(self):
        return self.__numero

    def get_credit(self):
        return self.__credit

    def add_credits(self, valeur):
        if valeur >= 0:
            self.__credit += valeur

    def studentEval(self):
        if self.get_credit() >= 90:
            return "Excellent"
        elif self.get_credit() >= 80:
            return "Très Bien"
        elif self.get_credit() >= 70:
            return "Bien"
        elif self.get_credit() >= 60:
            return "Passable"
        else:
            return "insuffisant"

    def studentInfos(self):
        print("Nom :", self.get_prenom(), "\nPrénom :", self.get_nom(),
              "\nID :", self.get_numero(), "\nNiveau :", self.studentEval())


student =Student("John", "Doe", "145")
student.add_credits((60))
student.add_credits((10))
student.add_credits((10))
print("Le nombre de crédits de", student.get_prenom(), student.get_nom(),
      "est de", student.get_credit(), "points")
student.studentInfos()






