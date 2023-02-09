from PokerPy import Card, Hand, calculate_hand_frequency, calculate_hand_heuristic, get_best_hand

def test_hand_init():
    all_cards = [Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4), Card(11, 2)]
    hand = Hand(8, all_cards)
    assert hand.hand_type == 8
    assert hand.Cards == all_cards
