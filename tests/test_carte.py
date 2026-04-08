from src.carte import Carte
from pytest import raises

def test_representation_formelle():
    carte = Carte(2, "PIQUE")
    assert repr(carte) == "Carte 2 de PIQUE"

    carte2 = Carte("AS", "COEUR")
    assert repr(carte2) == "Carte AS de COEUR"

    with raises(ValueError):
        Carte("JOKER", "NOIR")

    with raises(ValueError):
        Carte(10, "VIOLET")

