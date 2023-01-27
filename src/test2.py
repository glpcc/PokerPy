import PokerPy
from time import perf_counter_ns

def generate_random_hands(num_cards: int,num_players: int)-> list[list[PokerPy.Card]]:
    posible_cards = set()
    for i in range(4):
        for j in range(1,14):
            posible_cards.add(PokerPy.Card(j,i))
    res = []
    for i in range(num_players):
        player_cards = []
        for j in range(num_cards):
            card = posible_cards.pop()
            player_cards.append(card)
        res.append(player_cards)
    return res



test_hand = generate_random_hands(2,10) 
print(test_hand)
t1 = perf_counter_ns()
frecs = PokerPy.calculate_hand_frecuency(test_hand)
print(frecs)
for i in range(len(frecs)):
    print(f"Player {i}: Wins: {(frecs[i]['Win']/frecs[i]['Total Cases'])*100:.2f}% ,Draws: {(frecs[i]['Draw']/frecs[i]['Total Cases'])*100:.2f}%")
print(perf_counter_ns()-t1)

