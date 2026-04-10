from src.carte import Carte
from src.valeur import Valeur
from src.couleur import Couleur
import random

class Paquet:
    def __init__(self):
        self.cartes = []
        for couleur in Couleur:
            for valeur in Valeur:
                self.cartes.append(Carte(valeur, couleur))
    
    def shuffle(self):
        random.shuffle(self.cartes)