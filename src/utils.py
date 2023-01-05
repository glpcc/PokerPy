from __future__ import annotations
from dataclasses import dataclass
from math import comb

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
HAND_TYPES = {
    "Straight Flush":0,
    "Royal Flush":1,
    "Poker":2,
    "Full House":3,
    "Flush":4,
    "Straight":5,
    "Triples":6,
    "Double Pairs":7,
    "Pairs":8,
    "High Card":9
}
TOTAL_CARDS = 52
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



class Hand():
    def __init__(self,hand_type: str,cards: list[Card]) -> None:
        self.type = hand_type
        self.cards = cards
    
    def custom_compare(self,l: list[int]) -> bool:
        print(l)
        for i in range(0,len(l),2):
            if l[i] > l[i+1]:
                return True
            elif l[i] < l[i+1]:
                return False
        return False

    def compare_pos(self,other_hand: Hand,pos: list[int]):
        l = []
        for i in pos:
            if i < len(self.cards):
                l.append(CARD_VALUES[self.cards[i].value])
                l.append(CARD_VALUES[other_hand.cards[i].value])
        return self.custom_compare(l)
    
    def __eq__(self, other: Hand) -> bool:
        if self.type != other.type:
            return False
        if self.type == "Straight Flush" or self.type == "Straight":
            return self.cards[0].value == other.cards[0].value
        elif self.type == "Poker":
            return all(self.cards[i].value == other.cards[i].value for i in [0,4] if i < len(self.cards))
        elif self.type == "Full House":
            return self.cards[0].value == other.cards[0].value and self.cards[3].value == other.cards[3].value
        elif self.type == "Flush" or self.type == "High Card":
            return all(i.value == j.value for i,j in zip(self.cards,other.cards))
        elif self.type == "Triples":
            return all(self.cards[i].value == other.cards[i].value for i in [0,3,4] if i < len(self.cards))
        elif self.type == "Double Pairs":
            return all(self.cards[i].value == other.cards[i].value for i in [0,2,4] if i < len(self.cards))
        elif self.type == "Pairs":
            return all(self.cards[i].value == other.cards[i].value for i in [0,2,3,4] if i < len(self.cards))
        else:
            # Royal Flush
            return True

    def __gt__(self,other: Hand)-> bool:
        if self.type != other.type:
            return HAND_TYPES[self.type] > HAND_TYPES[other.type]
        if self.type == "Straight Flush" or self.type == "Straight":
            return self.compare_pos(other,[0])
        elif self.type == "Poker":
            return self.compare_pos(other,[0,4])
        elif self.type == "Full House":
            return self.compare_pos(other,[0,3])
        elif self.type == "Flush" or self.type == "High Card":
            return self.compare_pos(other,[0,1,2,3,4])
        elif self.type == "Straight":
            return self.compare_pos(other,[0])
        elif self.type == "Triples":
            return self.compare_pos(other,[0,3,4])
        elif self.type == "Double Pairs":
            return self.compare_pos(other,[0,2,4])
        elif self.type == "Pairs":
            return self.compare_pos(other,[0,2,3,4])
        else:
            # Royal Flush
            return False
    
    def __lt__(self,other: Hand)-> bool:
        return not self > other

    def __ge__(self,other: Hand)-> bool:
        return self == other or self > other
    
    def __le__(self,other: Hand)-> bool:
        return self == other or self < other
    
    def __repr__(self) -> str:
        return f'Hand(Hand_type: {self.type},Cards: {self.cards})'

def get_best_hand(cards: list[Card])-> Hand:
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
        if CARD_VALUES[last_card.value] - CARD_VALUES[i.value] == 1:
            straigth.append(i)
        else:
            straigth = [i]
        if len(straigth) == 5:
            straights.append(straigth)
            straigth = straigth[1:]
        last_card = i
    if len(straights) > 0:
        straight_flushes = [i for i in straights if all(j.color == i[0].color for j in i)]
        if len(straight_flushes) > 0:
            hand_type = "Straight Flush"
            hand = straight_flushes[0]
            if hand[0].value == 'A':
                hand_type = "Royal Flush"
            return Hand(hand_type,hand)

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
        return Hand(hand_type,hand)

    pairs = sorted(pairs,key= lambda k: k[0], reverse=True)
    triples = sorted(triples,key= lambda k: k[0], reverse=True)
    if len(triples) > 0 and len(pairs) > 0:
        hand_type = "Full House" 
        hand = triples[0] + pairs[0]
        return Hand(hand_type,hand)
    
    # WARNING no comparison between flushes is made cause no more than 7 cards are expected
    flushes = [colors_nums[i] for i in colors_nums if len(colors_nums[i])>=5]
    if len(flushes) > 0:
        hand_type = "Flush"
        hand = sorted(flushes[0],reverse=True)[0:5]
        return Hand(hand_type,hand)
    
    if len(straights) > 0:
        hand_type = "Straight"
        hand = straights[0]
        return Hand(hand_type,hand)
    
    if len(triples) > 0:
        hand_type = "Triples"
        hand = triples[0]
        if len(cards)-3 > 0:
            hand += individuals[0:min(2,len(cards)-3)]
        return Hand(hand_type,hand)  

    if len(pairs) >= 2:
        hand_type = "Double Pairs"
        hand = pairs[0] + pairs[1]
        if len(cards) > 4:
            hand.append(individuals[0])
        return Hand(hand_type,hand)
    
    if len(pairs) >= 1:
        hand_type = "Pairs"
        hand = pairs[0]
        if len(cards)-2 > 0:
            hand += individuals[0:min(3,len(cards)-2)]
        return Hand(hand_type,hand) 

    hand_type = 'High Card'
    if len(cards) > 5:
        hand = individuals[0:5]
    else:
        hand = individuals

    return Hand(hand_type,hand)



def get_flush_prob(hand: Hand)-> float:
    prob = 0
    color_cuant = {i:0 for i in COLORS}
    remaining_cards = 52 - len(hand.cards)
    cards_to_full = 7 - len(hand.cards)
    for card in hand.cards:
        color_cuant[card.color] += 1
    temp = 0
    for color in color_cuant:
        for i in range(cards_to_full-(4-color_cuant[color])):
            temp += comb(13-color_cuant[color],4-color_cuant[color]+i)*comb(remaining_cards-(13-color_cuant[color]),cards_to_full-i)
    return prob
h = get_best_hand([Card('C','7'),Card('D','9'),Card('H','7')])
print(get_flush_prob(h))
