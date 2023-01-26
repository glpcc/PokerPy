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



test_hand = generate_random_hands(2,5) 
print(test_hand)
t1 = perf_counter_ns()
print(PokerPy.calculate_hand_frecuency2(test_hand))
print(perf_counter_ns()-t1)
t1 = perf_counter_ns()
# print(PokerPy.calculate_hand_frecuency([a[0:2],a[2:4],a[4:6],a[6:8]]))
print(PokerPy.calculate_hand_frecuency(test_hand))
print(perf_counter_ns()-t1)

