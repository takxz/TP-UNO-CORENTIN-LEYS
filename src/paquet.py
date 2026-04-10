from src.carte import Carte
from src.valeur import Valeur
from src.couleur import Couleur


class Paquet:
    def __init__(self):
        self.cartes = []
        for valeur in Valeur:
            for couleur in Couleur:
                self.cartes.append(Carte(valeur, couleur))
    



