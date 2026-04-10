from src.carte import Carte
from src.valeur import Valeur

def main():
    carte = Carte("deux", "PIQUE")
    print(carte)
    print(carte.points())



if __name__ == "__main__":
    main()