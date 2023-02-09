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

    string to_string() const {
        return "Card: " + card_values[this->value - 1] + colors[this->suit - 1];
    }

    bool operator==(const Card& rhs) const {
        return (this->value == rhs.value) && (this->suit == rhs.suit);
    }

    bool operator>=(const Card& rhs) const {
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

    string to_string() const {
        string res = "Hand: " + hand_names[this->hand_type - 1] + ", Cards:";
        for (Card card: this->Cards){
            res += " " + card_values[card.value - 1] + colors[card.suit - 1];
        }
        return res;
    }

    int hand_heuristic() const {
        // Uses bitshifting to ensure ranking of hands. It is shifted in pacs of 4bits allowing 16 options (13 needed)
        int64_t result = this->hand_type;
        for (auto card: this->Cards)
        {
            result = result << 4;
            result += card.value;
        }
        return result;
    }

    bool operator==(const Hand& rhs) const {
        return (this->hand_type == rhs.hand_type) && (this->Cards == rhs.Cards);
    }

    bool operator>=(const Hand& rhs) const {
        return this->hand_heuristic() >= rhs.hand_heuristic();
    }
};

#endif