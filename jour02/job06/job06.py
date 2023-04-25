class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def get_marque(self):
        return self.marque
    def get_modele(self):
        return self.modele
    def get_annee(self):
        return self.annee
    def get_prix(self):
        return self.prix

    def informationVehicule(self):
        print("Marque :", self.get_marque())
        print("Modèle :",self.get_modele())
        print("Année :", self.get_annee())
        print("Prix :", self.get_prix())

    def demarrer(self):
        print("Attention je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def get_portes(self):
        return self.portes
    def informationVehicule(self):
        print("Marque :", self.get_marque())
        print("Modèle :", self.get_modele())
        print("Année :", self.get_annee())
        print("Prix :", self.get_prix())
        print("Nombre de porte :", self.get_portes())

    def demarrer(self):
        print("Attention je roule avec ma voiture")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def get_roues(self):
        return self.roues

    def informationVehicule(self):
        print("Marque :", self.get_marque())
        print("Modèle :", self.get_modele())
        print("Année :", self.get_annee())
        print("Prix :", self.get_prix())
        print("Nombre de roue :", self.get_roues())

    def demarrer(self):
        print("Attention je roule avec ma moto")



vehicule = Vehicule("Mercedes", "Classe A", "2020", 18500)
vehicule.informationVehicule()
vehicule.demarrer()
voiture = Voiture("Mercedes", "Classe A", "2020", 18500)
voiture.informationVehicule()
voiture.demarrer()
moto = Moto("Yamaha", "1200 Vmax", "1987", 4500)
moto.informationVehicule()
moto.demarrer()
