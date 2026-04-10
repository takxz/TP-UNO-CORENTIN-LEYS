from src.carte import Carte
from src.valeur import Valeur
from src.couleur import Couleur
import random

class Paquet:
    #Le constructeur de la classe Paquet crée un paquet de 52 cartes en combinant les valeurs et les couleurs
    def __init__(self):
        self.cartes = []
        for couleur in Couleur:
            for valeur in Valeur:
                self.cartes.append(Carte(valeur, couleur))
    
    #Utilisation de la fonction shuffle du module random pour mélanger les cartes
    def shuffle(self):
        random.shuffle(self.cartes)

    #Utilisation de la fonction randint pour couper le paquet à un endroit aléatoire
    def cut(self):
        nb_aleatoire = random.randint(1, 50)
        carte_coupee = self.cartes[:nb_aleatoire]
        self.cartes = self.cartes[nb_aleatoire:] + carte_coupee

    #La méthode piocher utilise la méthode pop pour retirer la première carte du paquet et la retourner
    def piocher(self):
        x = self.cartes.pop(0)
        return x
    
    #Distribution des cartes
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
        
