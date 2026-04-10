from src.valeur import Valeur
from src.couleur import Couleur

class Carte:
    #Le constructeur de la classe Carte vérifie que les arguments sont valides et les convertit en enums si nécessaire
    def __init__(self, valeur, couleur):
        if isinstance(valeur, str):
            try:
                valeur = Valeur[valeur.upper()]
            except KeyError as e:
                raise ValueError("Valeur de carte invalide") from e
        elif not isinstance(valeur, Valeur):
            raise ValueError("Valeur de carte invalide")

        if isinstance(couleur, str):
            try:
                couleur = Couleur[couleur.upper()]
            except KeyError as e:
                raise ValueError("Couleur de carte invalide") from e
        elif not isinstance(couleur, Couleur):
            raise ValueError("Couleur de carte invalide")

        self.valeur = valeur
        self.couleur = couleur

    #Utilisation d'un switch pour afficher les valeurs textes des cartes
    def __repr__(self):
        match self.valeur:
            case Valeur.AS:
                    valeur_affichee = "AS"
            case Valeur.VALET:
                    valeur_affichee = "VALET"
            case Valeur.DAME:
                    valeur_affichee = "DAME"
            case Valeur.ROI:
                    valeur_affichee = "ROI"
            case _:
                    valeur_affichee = str(self.valeur.value)
            
        return f"<Carte {valeur_affichee} de {self.couleur.value}>"
    
    #Utilisation de la valeur de l'enum pour calculer les points de la carte
    def points(self):
        return self.valeur.value