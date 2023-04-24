class Livre:
    def __init__(self):
        self.__titre = "Shining"
        self.__auteur = "Stephen King"
        self.__nbr_pg = 576
        self.__dispo = True

    def vérification(self):
        if self.get_dispo() == True:
            return True
        else:
            return False

    def emprunter(self):
        if self.get_dispo() == True:
            print("Le livre est disponible")
            self.__dispo = False
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.get_dispo() == False:
            self.__dispo = True
            print("livre rendu")


    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nbr_pg(self):
        return self.__nbr_pg
    def get_dispo(self):
        pass



    def set_infos(self, titre, auteur, nbr_pg):
        self.__titre = titre
        self.__auteur = auteur
        if nbr_pg >= 0:
            self.__nbr_pg = nbr_pg
        else:
            self.__nbr_pg = "\n  !!! erreur, le nombre de page doit être un nombre entier positif !!!"

livre = Livre()
#print("Le titre du livre est", livre.get_titre(), ", l'auteur est", livre.get_auteur(),
      #"et le nombre de pages est de", livre.get_nbr_pg())
#livre.set_infos("Player One", "Ernest Cline", 560)
#print("Le titre du livre est", livre.get_titre(), ", l'auteur est", livre.get_auteur(),
      #"et le nombre de pages est de", livre.get_nbr_pg())
#print(livre.vérification())