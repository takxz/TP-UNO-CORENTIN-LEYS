from src.carte import Carte
from src.valeur import Valeur
from src.paquet import Paquet

def main():
    carte = Carte("trois", "PIQUE")
    print(carte)
    print(carte.points())

    paquet = Paquet()
    print(paquet)



if __name__ == "__main__":
    main()