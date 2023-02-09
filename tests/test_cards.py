from PokerPy import Card

def test_card_init():
    card = Card('KD')
    assert card.value == 12
    assert card.suit == 2

def test_card_eq():
    assert Card('KD') == Card('KD')
    assert Card('KD') != Card('AD')
    assert Card('KD') != Card('KS')
    assert Card('KD') != Card('AS')