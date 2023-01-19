from utils import Card,get_best_hand,CARD_VALUES,COLORS,HAND_TYPES
from math import comb
from itertools import combinations
from cProfile import Profile
all_cards = []
for i in COLORS:
    all_cards += [Card(i,v) for v in CARD_VALUES]


a_hand = [Card('H','A'),Card('C','3')]
left_cards = [i for i in all_cards if i not in a_hand]
print(left_cards)
hands_types_frecuency = {h:0 for h in HAND_TYPES}

for new_cards in combinations(left_cards,5):
    hand = get_best_hand(a_hand + list(new_cards))
    hands_types_frecuency[hand.type] += 1

# print(pr.print_stats(sort='tottime'))

print(hands_types_frecuency)
print(sum(hands_types_frecuency[i] for i in hands_types_frecuency))
print(len(left_cards))
print(comb(50,5))