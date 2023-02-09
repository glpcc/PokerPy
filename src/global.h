#ifndef _GLOBAL_H
#define _GLOBAL_H

#include <string>
#include <array>
#include <map>

using namespace std;

enum Suit {Hearts = 1, Diamonds, Clubs, Spades = 4};
enum HandType {
    HighCard = 1,
    Pairs,
    DoublePairs,
    Triples,
    Straight,
    Flush,
    FullHouse,
    Poker,
    StraightFlush,
    RoyalFlush = 10
};
array<string, 4> colors = {"♥", "♦", "♣", "♠"};
array<string, 13> card_values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
map<string, Suit> suit_values = {{"♥", Hearts}, {"♦", Diamonds}, {"♣", Clubs}, {"♠", Spades}, {"H", Hearts}, {"D", Diamonds}, {"C", Clubs}, {"S", Spades}};
map<string, short> card_values_nums = {{"2", 1}, {"3", 2}, {"4", 3}, {"5", 4}, {"6", 5}, {"7", 6}, {"8", 7}, {"9", 8}, {"10", 9}, {"J", 10}, {"Q", 11}, {"K", 12}, {"A", 13}};
array<string,10> hand_names = {
    "High Card",
    "Pairs",
    "Double Pairs",
    "Triples",
    "Straight",
    "Flush",
    "Full House",
    "Poker",
    "Straight Flush",
    "Royal Flush"
};

struct Card{
    // 1 to 13 (2 to A)
    short value;
    // 0 to 3 (H to D)
    Suit suit;

    Card():
        value(0),
        suit((Suit) 0)
    {}

    Card(short value, short suit):
        value(value),
        suit((Suit) suit)
    {}

    bool operator==(Card& rhs){
        return (this->value == rhs.value) && (this->suit == rhs.suit);
    }

    bool operator>=(Card& rhs){
        if(this->value >= rhs.value){
            return true;
        } else {
            return this->suit >= rhs.suit;
        }
    }
};

struct Hand{
    HandType hand_type;
    array<Card,5> Cards;
    
    Hand():
        hand_type(HighCard),
        Cards()
    {}

    Hand(short hand_type, array<Card,5> cards):
        hand_type((HandType) hand_type),
        Cards(cards)
    {}

    int hand_heuristic(){
        // Uses bitshifting to ensure ranking of hands. It is shifted in pacs of 4bits allowing 16 options (13 needed)
        int64_t result = this->hand_type;
        switch (this->hand_type)
        {
            case RoyalFlush:
                result = result << 5*4;
                break;
            case StraightFlush:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4*4;
                break;
            case Poker:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4;
                result += this->Cards[4].value;
                result = result << 3*4;
                break;
            case FullHouse:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4;
                result += this->Cards[3].value;
                result = result << 3*4;
                break;
            case Flush:
                result = result << 4;
                for (int i = 0; i < 4; i++)
                {
                    result += this->Cards[i].value;
                    result = result << 4;
                }
                result += this->Cards[4].value;
                break;
            case Straight:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4*4;
                break;
            case Triples:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4;
                result += this->Cards[3].value;
                result = result << 4;
                result += this->Cards[4].value;
                result = result << 4*2;
                break;
            case DoublePairs:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4;
                result += this->Cards[2].value;
                result = result << 4;
                result += this->Cards[4].value;
                result = result << 4*2;
                break;
            case Pairs:
                result = result << 4;
                result += this->Cards[0].value;
                result = result << 4;
                for (int i = 0; i < 3; i++)
                {
                    result += this->Cards[i+2].value;
                    result = result << 4;
                }
                break;
            case HighCard:
                result = result << 4;
                for (int i = 0; i < 4; i++)
                {
                    result += this->Cards[i].value;
                    result = result << 4;
                }
                result += this->Cards[4].value;
                break;
        }
        return result;
    }
};

#endif