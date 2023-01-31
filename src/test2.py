import PokerPy
from time import perf_counter_ns
import random

random.seed(11)
HAND_TYPES = {
    "Royal Flush":1,
    "Straight Flush":0,
    "Poker":2,
    "Full House":3,
    "Flush":4,
    "Straight":5,
    "Triples":6,
    "Double Pairs":7,
    "Pairs":8,
    "High Card":9
}

def generate_random_hands(num_cards: int,num_players: int)-> list[list[PokerPy.Card]]:
    posible_cards = set()
    for i in range(4):
        for j in range(1,14):
            posible_cards.add(PokerPy.Card(j,i))
    res = []
    fold = []
    if num_cards > 2:
        for j in range(num_cards-2):
            card = random.choice(list(posible_cards))
            posible_cards.remove(card)
            fold.append(card)
    for i in range(num_players):
        player_cards = []
        for j in range(2):
            card = random.choice(list(posible_cards))
            posible_cards.remove(card)
            player_cards.append(card)
        player_cards += fold
        res.append(player_cards)
    return res


test_hand = PokerPy.Hand('Straight',[PokerPy.Card(12,1),PokerPy.Card(11,3),PokerPy.Card(10,0),PokerPy.Card(9,0),PokerPy.Card(8,0)])

print(PokerPy.calculate_hand_heuristic(test_hand))



num_players = 2
test_hand = generate_random_hands(2,num_players)
print(test_hand)
test = sorted([PokerPy.Card(12,1),PokerPy.Card(8,3),PokerPy.Card(12,0),PokerPy.Card(13,0),PokerPy.Card(3,0),PokerPy.Card(2,1),PokerPy.Card(1,1)],key=lambda k: k.value, reverse=True)
print(test)
print(PokerPy.get_best_hand(test).Cards)
print(PokerPy.get_best_hand(test).hand_type)
t1 = perf_counter_ns()
frecs = PokerPy.calculate_hand_frecuency(test_hand)
print(frecs)
for i in range(len(frecs)):
    print(f"Player {i}: Wins: {(frecs[i]['Win']/frecs[i]['Total Cases'])*100:.2f}% ,Draws: {(frecs[i]['Draw']/frecs[i]['Total Cases'])*100:.2f}%")
a = '\t'
for i in HAND_TYPES:
    print(f"{i}:{a*(1 if len(i) > 5 else 2)}",end="")
    for j in range(num_players):
        print(f"{(frecs[j][i]/frecs[j]['Total Cases'])*100:.2f}%\t",end="")
    print()
print(test_hand)
print(perf_counter_ns()-t1)

