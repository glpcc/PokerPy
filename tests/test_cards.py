from PokerPy import Card

def test_card_init():
    card = Card(12, 2)
    assert card.value == 12
    assert card.suit == 2

def test_card_from_string():
    card = Card.from_string('AD')
    assert card.value == 13
    assert card.suit == 2

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