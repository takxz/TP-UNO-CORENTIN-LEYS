from src.paquet import Paquet


def test_initialisation():
    paquet = Paquet()
    assert len(paquet.cartes) == 52