from src.carte import Carte
from src.valeur import Valeur
from src.paquet import Paquet

def main():
    carte = Carte("trois", "PIQUE")
    print(carte)
    print(f"Points: {carte.points()}")

    paquet = Paquet()
    paquet.shuffle()
    paquet.cut()
    carte_piochee = paquet.piocher()
    print(f"Carte piochée: {carte_piochee}")
    print(f"Points de la carte piochée: {carte_piochee.points()}")
    print(f"Nombre de cartes restantes dans le paquet: {len(paquet.cartes)}")
    mains = paquet.distribuer(5, 4)
    for i, main in enumerate(mains):
        print(f"Main du joueur {i + 1}:")
        for carte in main:
            print(f"{carte}")

if __name__ == "__main__":
    main()