from __future__ import annotations
from dataclasses import dataclass

CARD_VALUES = {
    "2":1,
    "3":2,
    "4":3,
    "5":4,
    "6":5,
    "7":6,
    "8":7,
    "9":8,
    "10":9,
    "J":10,
    "Q":11,
    "K":12,
    "A":13
}
COLORS = {'S','H','D','C'}
# Test to try to start to program the game
@dataclass
class Card():
    color: str
    value: str

    def __ge__(self, other: Card) -> bool:
        return CARD_VALUES[self.value] >= CARD_VALUES[other.value]

    def __le__(self, other: Card) -> bool:
        return CARD_VALUES[self.value] <= CARD_VALUES[other.value]

    def __gt__(self, other: Card) -> bool:
        return CARD_VALUES[self.value] > CARD_VALUES[other.value]

    def __lt__(self, other: Card) -> bool:
        return CARD_VALUES[self.value] < CARD_VALUES[other.value]

    def __repr__(self) -> str:
        return f'{self.value}{self.color}'

def get_best_hand(cards: list[Card]):
    hand = []
    # Count the number of values and color to check for pairs,triples,pokers or colors
    colors_nums: dict[str,list[Card]] = dict()
    value_nums: dict[str,list[Card]] = dict()
    for i in cards:
        if i.value in value_nums:
            value_nums[i.value].append(i)
        else:
            value_nums[i.value] = [i]
        
        if i.color in colors_nums:
            colors_nums[i.color].append(i)
        else:
            colors_nums[i.color] = [i]
        


    # Check for straights
    sorted_cards = sorted(cards, reverse=True)
    last_card = sorted_cards[0]
    straigth = [sorted_cards[0]]
    straights: list[list[Card]] = []
    for i in sorted_cards[1:]:
        if len(straigth) == 5:
            straights.append(straigth)
            straigth = straigth[1:]
        if CARD_VALUES[last_card.value] - CARD_VALUES[i.value] == 1:
            straigth.append(i)
        else:
            straigth = [i]
        last_card = i

    if len(straights) > 0:
        straight_flushes = [i for i in straights if all(j.color == i[0].color for j in i)]
        if len(straight_flushes) > 0:
            hand_type = "Straight Flush"
            hand = straight_flushes[0]
            if hand[0].value == 'A':
                hand_type = "Royal Flush"
            return hand, hand_type

    triples = []
    pairs = []
    individuals = []
    pokers = []
    for i in value_nums:
        if len(value_nums[i]) == 1:
            individuals.append(value_nums[i][0])
        elif len(value_nums[i]) == 2:
            pairs.append(value_nums[i])
        elif len(value_nums[i]) == 3:
            triples.append(value_nums[i])
        else:
            pokers.append(value_nums[i])
    individuals = sorted(individuals,reverse=True)

    if len(pokers) > 0:
        hand_type = "Poker"
        hand = sorted(pokers,key= lambda k: k[0], reverse=True)[0]
        if len(cards) > 4:
            hand.append(individuals[0])
        return hand,hand_type

    pairs = sorted(pairs,key= lambda k: k[0], reverse=True)
    triples = sorted(triples,key= lambda k: k[0], reverse=True)
    if len(triples) > 0 and len(pairs) > 0:
        hand_type = "Full House" 
        hand = triples[0] + pairs[0]
        return hand, hand_type
    
    # WARNING no comparison between flushes is made cause no more than 7 cards are expected
    flushes = [colors_nums[i] for i in colors_nums if len(colors_nums[i])>=4]
    if len(flushes) > 0:
        hand_type = "Flush"
        hand = sorted(flushes[0],reverse=True)[0:4]
        return hand, hand_type
    
    if len(straights) > 0:
        hand_type = "Straight"
        hand = straights[0]
        return hand, hand_type
    
    if len(triples) > 0:
        hand_type = "Triples"
        hand = triples[0]
        if len(cards)-3 > 0:
            hand += individuals[0:len(cards)-3]
        return hand, hand_type  

    if len(pairs) >= 2:
        hand_type = "Double Pairs"
        hand = pairs[0] + pairs[1]
        if len(cards) > 4:
            hand.append(individuals[0])
        return hand, hand_type  
    
    if len(pairs) >= 1:
        hand_type = "Pairs"
        hand = pairs[0]
        if len(cards)-2 > 0:
            hand += individuals[0:len(cards)-2]
        return hand, hand_type  

    hand_type = 'High Card'
    if len(cards) > 5:
        hand = individuals[0:5]
    else:
        hand = individuals

    return hand, hand_type

    

        




    
    

    
# Spades, Hearts, Diamonds, Clubs
test_hand = [Card('C','9'),Card('D','8'),Card('H','K'),Card('H','A'),Card('S','8')]
print(get_best_hand(test_hand))