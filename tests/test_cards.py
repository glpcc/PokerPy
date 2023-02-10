from PokerPy import Card

def test_card_init():
    card = Card(12, 2)
    assert card.value == 'K'
    assert card.suit == '♦'

def test_card_from_string():
    card = Card('AD')
    assert card.value == 'A'
    assert card.suit == '♦'

def test_card_repr():
    card = Card(12, 2)
    assert card.__repr__() == "Card: K♦"

def test_card_eq():
    assert Card(12, 2) == Card(12, 2)
    assert Card(12, 2) != Card(13, 2)
    assert Card(12, 2) != Card(12, 1)
    assert Card(12, 2) != Card(13, 1)

def test_card_ge():
    assert Card(12, 2) >= Card(11, 2)
    assert Card(12, 2) >= Card(12, 1)