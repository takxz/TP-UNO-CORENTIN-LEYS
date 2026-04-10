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

    def cut(self):
        nb_aleatoire = random.choice([1, 50])
        carte_coupee = self.cartes[:nb_aleatoire]
        self.cartes = self.cartes[nb_aleatoire:] + carte_coupee

    def piocher(self):
        x = self.cartes.pop(0)
        return x
    
    def distribuer(self, nb_cartes, nb_joueurs):
        if nb_cartes * nb_joueurs > len(self.cartes):
            raise ValueError("Pas assez de cartes pour distribuer")
        main_joueurs = []
        for _ in range(nb_joueurs):
            main = []
            for _ in range(nb_cartes):
                main.append(self.piocher())
            main_joueurs.append(main)
        return main_joueurs
        
