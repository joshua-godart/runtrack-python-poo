class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = 5
        self.__en_marche = False

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage

    def get_reservoir_value(self):
        return self.__reservoir
    def get_state(self):
        return self.__en_marche

    def set_marque(self, new_marque):
        self.__marque = new_marque
    def set_modele(self, new_modele):
        self.__modele = new_modele
    def set_annee(self, new_annee):
        self.__annee = new_annee
    def set_kilometrage(self,new_kilometrage):
        self.__kilometrage = new_kilometrage

    def set_reservoir_value(self, new_reservoir_value):
        self.__reservoir = new_reservoir_value
    def set_state(self, new_state):
        self.__en_marche = new_state

    def verifier_plein(self, plein):
        pass


    def demarrer(self):
        if self.get_reservoir_value() > 5:
            self.__en_marche = True
            print("la voiture à démarrer")
        else:
            self.__en_marche = False
            print("pas assez d'essence")

    def arreter(self):
        self.__en_marche = False
        print("la voiture s'est arrêtée")

voiture = Voiture("renault", "clio", "2006", 95000)
voiture.demarrer()
voiture.arreter()



