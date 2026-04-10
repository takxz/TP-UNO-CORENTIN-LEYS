from src.paquet import Paquet


def test_initialisation():
    paquet = Paquet()
    assert len(paquet.cartes) == 52

def test_ordre_carte():
    paquet = Paquet()
    assert repr(paquet.cartes[0]) == "Carte AS de COEUR"
    assert repr(paquet.cartes[1]) == "Carte 2 de COEUR"
    assert repr(paquet.cartes[12]) == "Carte ROI de COEUR"
    assert repr(paquet.cartes[13]) == "Carte AS de CARREAU"
    assert repr(paquet.cartes[25]) == "Carte ROI de CARREAU"
    assert repr(paquet.cartes[26]) == "Carte AS de PIQUE"
    assert repr(paquet.cartes[38]) == "Carte ROI de PIQUE"
    assert repr(paquet.cartes[39]) == "Carte AS de TREFLE"
    assert repr(paquet.cartes[51]) == "Carte ROI de TREFLE"

def test_shuffle():
    paquet = Paquet()
    cartes_avant_shuffle = paquet.cartes.copy()
    paquet.shuffle()
    assert paquet.cartes != cartes_avant_shuffle