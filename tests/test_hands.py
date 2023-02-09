from PokerPy import Card, Hand

def test_hand_init():
    all_cards = [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    hand = Hand(8, all_cards)
    assert hand.hand_type == 8
    assert hand.Cards == all_cards

def test_calculate_hand_heuristic():
    test_hand = Hand(2, [Card(8, 1),Card(8, 3),Card(13, 3),Card(9, 1),Card(3, 3)])
    test_heuristic = 2677040
    assert test_heuristic == test_hand.hand_heuristic()

    test_hand = Hand(10, [Card(9, 1),Card(10, 1),Card(11, 1),Card(12, 1),Card(13, 1)])
    test_heuristic = 10485760
    assert test_heuristic == test_hand.hand_heuristic()