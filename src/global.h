#ifndef _GLOBAL_H
#define _GLOBAL_H

#include <string>
#include <array>
#include <map>

using namespace std;

enum Suit {Hearts = 1, Diamonds, Clubs, Spades};
array<string, 4> colors = {"♣","♦","♥","♠"};
array<string, 13> card_values = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"};
map<string, Suit> suit_values = {{"♥", Hearts}, {"♦", Diamonds}, {"♣", Clubs}, {"♠", Spades}, {"H", Hearts}, {"D", Diamonds}, {"C", Clubs}, {"S", Spades}};
map<string, int> card_values_nums = {{"2",1},{"3",2},{"4",3},{"5",4},{"6",5},{"7",6},{"8",7},{"9",8},{"10",9},{"J",10},{"Q",11},{"K",12},{"A",13}};
map<string, int> hand_value = {
    {"Royal Flush",10},{"Straight Flush",9},{"Poker",8},{"Full House",7},{"Flush",6},{"Straight",5},{"Triples",4},{"Double Pairs",3},{"Pairs",2},{"High Card",1}
};
array<string,10> hands = {"Royal Flush","Straight Flush","Poker","Full House","Flush","Straight","Triples","Double Pairs","Pairs","High Card"};

struct Card{
    // 1 to 13 (2 to A)
    short value;
    // 0 to 3 (H to D)
    Suit suit;
};

struct Hand{
    string hand_type;
    array<Card,5> Cards;
};

#endif