from PokerPy import Card

def test_card_init():
    card = Card(12, 2)
    assert card.value == 12
    assert card.suit == 2

def test_card_eq():
    assert Card(12, 2) == Card(12, 2)
    assert Card(12, 2) != Card(13, 2)
    assert Card(12, 2) != Card(12, 1)
    assert Card(12, 2) != Card(13, 1)