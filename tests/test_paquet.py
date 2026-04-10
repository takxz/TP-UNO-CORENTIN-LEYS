from src.paquet import Paquet
from pytest import raises

def test_initialisation():
    paquet = Paquet()
    assert len(paquet.cartes) == 52

def test_ordre_carte():
    paquet = Paquet()
    assert repr(paquet.cartes[0]) == "<Carte AS de COEUR>"
    assert repr(paquet.cartes[1]) == "<Carte 2 de COEUR>"
    assert repr(paquet.cartes[12]) == "<Carte ROI de COEUR>"
    assert repr(paquet.cartes[13]) == "<Carte AS de CARREAU>"
    assert repr(paquet.cartes[25]) == "<Carte ROI de CARREAU>"
    assert repr(paquet.cartes[26]) == "<Carte AS de PIQUE>"
    assert repr(paquet.cartes[38]) == "<Carte ROI de PIQUE>"
    assert repr(paquet.cartes[39]) == "<Carte AS de TREFLE>"
    assert repr(paquet.cartes[51]) == "<Carte ROI de TREFLE>"

def test_shuffle():
    paquet = Paquet()
    cartes_avant_shuffle = paquet.cartes.copy()
    paquet.shuffle()
    assert paquet.cartes != cartes_avant_shuffle

def test_cut():
    paquet = Paquet()
    cartes_avant_cut = paquet.cartes.copy()
    paquet.cut()
    assert paquet.cartes != cartes_avant_cut

def test_piocher():
    paquet = Paquet()
    carte_piochee = paquet.piocher()
    assert repr(carte_piochee) == "<Carte AS de COEUR>"
    assert len(paquet.cartes) == 51

    paquet2 = Paquet()
    paquet2.shuffle()
    carte_piochee2 = paquet2.piocher()
    assert repr(carte_piochee2) != "<Carte AS de COEUR>"
    assert len(paquet2.cartes) == 51


def test_distribuer():
    paquet = Paquet()
    mains = paquet.distribuer(5, 4)
    assert len(mains) == 4
    for main in mains:
        assert len(main) == 5
    assert len(paquet.cartes) == 52 - 5 * 4

    paquet2 = Paquet()
    with raises(ValueError):
        paquet2.distribuer(10, 6)
