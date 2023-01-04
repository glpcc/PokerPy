from utils import Card,get_best_hand
# Spades, Hearts, Diamonds, Clubs
center_cards = [Card('C','7'),Card('C','9'),Card('H','7'),Card('C','Q'),Card('C','J')]
a_hand = [Card('C','8'),Card('C','6')]
b_hand = [Card('C','10'),Card('C','7')]

print(get_best_hand(a_hand+center_cards))
print(get_best_hand(b_hand+center_cards))
print(get_best_hand(a_hand+center_cards) >= get_best_hand(b_hand+center_cards))