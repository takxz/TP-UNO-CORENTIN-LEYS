from src.carte import Carte
from src.valeur import Valeur
from src.paquet import Paquet

def main():
    carte = Carte("trois", "PIQUE")
    print(carte)
    print(carte.points())

    paquet = Paquet()
    paquet.shuffle()
    paquet.cut()
    carte_piochee = paquet.piocher()
    print(carte_piochee)
    print(carte_piochee.points())
    



if __name__ == "__main__":
    main()