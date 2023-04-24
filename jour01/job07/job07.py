class Livre:
    def __init__(self):
        self.__titre = "Shining"
        self.__auteur = "Stephen King"
        self.__nbr_pg = 576

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nbr_pg(self):
        return self.__nbr_pg

    def set_infos(self, titre, auteur, nbr_pg):
        self.__titre = titre
        self.__auteur = auteur
        if nbr_pg >= 0:
            self.__nbr_pg = nbr_pg
        else:
            self.__nbr_pg = "erreur"
            print("le nombre de page doit être un nombre entier positif")

livre = Livre()
print("Le titre du livre est", livre.get_titre(), ", l'auteur est", livre.get_auteur(),
      "et le nombre de pages est de", livre.get_nbr_pg())
livre.set_infos("Player One", "Ernest Cline", 650)
print("Le titre du livre est", livre.get_titre(), ", l'auteur est", livre.get_auteur(),
      "et le nombre de pages est de", livre.get_nbr_pg())