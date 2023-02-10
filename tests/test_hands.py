from PokerPy import Card, Hand

def test_hand_init():
    all_cards = [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    hand = Hand(8, all_cards)
    assert hand.hand_type == 8
    assert hand.Cards == all_cards

def test_hand_init_from_string():
    all_cards = [Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('QD')]
    hand = Hand("Poker", all_cards)
    assert hand.hand_type == 8
    assert hand.Cards == all_cards

def test_hand_repr():
    hand = Hand(8, [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)])
    assert hand.__repr__() == "Hand: Poker, Cards: K♥ K♦ K♣ K♠ Q♦"

def test_hand_eq():
    poker_cards = [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    fh_cards = [Card(11, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    assert Hand(8, poker_cards) == Hand(8, poker_cards)
    assert Hand(7, poker_cards) != Hand(8, poker_cards)
    assert Hand(8, poker_cards) != Hand(7, fh_cards)

def test_hand_ge():
    rf_cards = [Card(9, 1),Card(10, 1),Card(11, 1),Card(12, 1),Card(13, 1)]
    poker_cards = [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    fh_cards = [Card(11, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    assert Hand(8, poker_cards) >= Hand(8, poker_cards)
    assert Hand(7, poker_cards) >= Hand(7, fh_cards)
    assert Hand(10, rf_cards) >= Hand(8, poker_cards)

def test_calculate_hand_heuristic():
    test_hand = Hand(2, [Card(8, 1),Card(8, 3),Card(13, 3),Card(9, 1),Card(3, 3)])
    test_heuristic = 2657683
    assert test_heuristic == test_hand.hand_heuristic()

    test_hand = Hand(10, [Card(9, 1),Card(10, 1),Card(11, 1),Card(12, 1),Card(13, 1)])
    test_heuristic = 11119565
    assert test_heuristic == test_hand.hand_heuristic()