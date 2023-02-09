from PokerPy import Card, Hand, calculate_hand_frequency, calculate_hand_heuristic, get_best_hand

def test_calculate_frec():
    test_cards = [[Card('KD'),Card('9H')],[Card('KC'),Card('AC')]]
    frecs = calculate_hand_frequency(test_cards)
    test_frecs = [
        {'Double Pairs': 355878, 'Draw': 20234, 'Flush': 38643, 'Full House': 28846, 'High Card': 358523, 'Pairs': 784240, 'Poker': 1430, 'Royal Flush': 46, 'Straight': 77914, 'Straight Flush': 284, 'Total Cases': 1712305, 'Triples': 66500, 'Win': 380882},
        {'Double Pairs': 347144, 'Draw': 20234, 'Flush': 124371, 'Full House': 28846, 'High Card': 337972, 'Pairs': 747226, 'Poker': 1430, 'Royal Flush': 992, 'Straight': 59303, 'Straight Flush': 70, 'Total Cases': 1712305, 'Triples': 64950, 'Win': 1311188}
    ]
    assert frecs == test_frecs

def test_best_hand():
    test_cards = [Card('KD'),Card('9H'),Card('KC'),Card('AC'),Card('4C'),Card('3D'),Card('2D')]
    best_hand = get_best_hand(test_cards)
    test_hand = Hand("Pairs",[Card('KD'),Card('KC'),Card('AC'),Card('9H'),Card('4C')])
    assert test_hand.hand_type == best_hand.hand_type
    assert test_hand.Cards == best_hand.Cards

def test_calculate_hand_heuristic():
    test_hand = Hand("Pairs",[Card('9H'),Card('9C'),Card('AC'),Card('10H'),Card('4C')])
    test_heuristic = 2677040
    assert test_heuristic == calculate_hand_heuristic(test_hand)
