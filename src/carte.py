

class Carte:
    def __init__(self, valeur, couleur):
        if valeur not in [2, 3, 4, 5, 6, 7, 8, 9, 10, "VALET", "DAME", "ROI", "AS"]:
            raise ValueError("Valeur de carte invalide")
        if couleur not in ["COEUR", "CARREAU", "PIQUE", "TREFLE"]:
            raise ValueError("Couleur de carte invalide")
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"Carte {self.valeur} de {self.couleur}"