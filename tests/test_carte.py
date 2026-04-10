from src.carte import Carte
from pytest import raises

def test_representation_formelle():
    carte = Carte("DEUX", "PIQUE")
    assert repr(carte) == "<Carte 2 de PIQUE>"

    carte2 = Carte("AS", "COEUR")
    assert repr(carte2) == "<Carte AS de COEUR>"

    carte3 = Carte("VALET", "CARREAU")
    assert repr(carte3) == "<Carte VALET de CARREAU>"

    with raises(ValueError):
        Carte("JOKER", "NOIR")

    with raises(ValueError):
        Carte(10, "VIOLET")

def test_points():
    carte = Carte("DEUX", "PIQUE")
    assert carte.points() == 2

    carte2 = Carte("AS", "COEUR")
    assert carte2.points() == 1

    carte3 = Carte("VALET", "CARREAU")
    assert carte3.points() == 11
