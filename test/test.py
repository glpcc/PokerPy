import PokerPy
import unittest
from time import perf_counter

class module_tests(unittest.TestCase):
    def test_calculate_frec(self):
        test_cards = [[PokerPy.Card('KD'),PokerPy.Card('9H')],[PokerPy.Card('KC'),PokerPy.Card('AC')]]
        frecs = PokerPy.calculate_hand_frecuency(test_cards)
        test_frecs = [{'Double Pairs': 355878, 'Draw': 20234, 'Flush': 38643, 'Full House': 28846, 'High Card': 358523, 'Pairs': 784240, 'Poker': 1430, 'Royal Flush': 46, 'Straight': 77914, 'Straight Flush': 284, 'Total Cases': 1712305, 'Triples': 66500, 'Win': 380882}, {'Double Pairs': 347144, 'Draw': 20234, 'Flush': 124371, 'Full House': 28846, 'High Card': 337972, 'Pairs': 747226, 'Poker': 1430, 'Royal Flush': 992, 'Straight': 59303, 'Straight Flush': 70, 'Total Cases': 1712305, 'Triples': 64950, 'Win': 1311188}]
        self.assertEqual(frecs,test_frecs)
    
    def test_best_hand(self):
        test_cards = [PokerPy.Card('KD'),PokerPy.Card('9H'),PokerPy.Card('KC'),PokerPy.Card('AC'),PokerPy.Card('4C'),PokerPy.Card('3D'),PokerPy.Card('2D')]
        best_hand = PokerPy.get_best_hand(test_cards)
        test_hand = PokerPy.Hand("Pairs",[PokerPy.Card('KD'),PokerPy.Card('KC'),PokerPy.Card('AC'),PokerPy.Card('9H'),PokerPy.Card('4C')])
        self.assertEqual(test_hand.hand_type,best_hand.hand_type)
        self.assertEqual(test_hand.Cards,best_hand.Cards)

    def test_calculate_hand_heuristic(self):
        test_hand = PokerPy.Hand("Pairs",[PokerPy.Card('9H'),PokerPy.Card('9C'),PokerPy.Card('AC'),PokerPy.Card('10H'),PokerPy.Card('4C')])
        test_heuristic = 2677040
        self.assertEqual(test_heuristic,PokerPy.calculate_hand_heuristic(test_hand))

