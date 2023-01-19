#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

struct Card{
    // 1 to 13 (2 to A)
    int value;
    // 1 to 4 (H to D)
    int color;
};

struct Hand{
    string hand_type;
    vector<Card> Cards;
};

void print_vector(vector<Card> cards){
    for(auto i=cards.begin(); i<cards.end(); i++)
	{
		cout<<(*i).value << " " << (*i).color << "\n";
	}
}

Hand get_best_hand(vector<Card> cards){
    // Sort the cards
    sort(cards.begin(),cards.end(),[](Card &a,Card &b){return a.value > b.value;});
    // Divide the cards by color
    map<int,vector<Card>> color_cards;
    // To get the straights
    vector<Card> current_straight = {cards[0]};
    vector<vector<Card>> straights;
    // To get rest of groupings
    vector<vector<Card>> pairs;
    vector<vector<Card>> triples;
    vector<Card> pokers;
    vector<Card> individuals;
    // Temporary variables;
    vector<Card> group = {cards[0]};
    Card last_card = cards[0];
    for(auto i=cards.begin()+1; i<cards.end(); i++)
	{
        if ((*i).value == last_card.value){
            group.push_back(*i);
        }else{
            switch (group.size())
            {
            case 1:
                individuals.push_back(last_card);
                break;
            case 2:
                pairs.push_back(group);
                break;
            case 3:
                triples.push_back(group);
                break;
            case 4:
                pokers = group;
                break;
            }
            group.clear();
            group.push_back(*i);
        }
        if ((*i).value - last_card.value == 1){
            current_straight.push_back(*i);
        }else if ((*i).value != last_card.value){
            current_straight.clear();
            current_straight.push_back(*i);
        }
        if (current_straight.size() == 5){
            straights.push_back(str)
        }
		cout<<(*i).value << " " << (*i).color << "\n";
	}

    print_vector(cards);
}

int main(){
    Card a;
    a.color = 1;
    a.value = 2;
    Card b;
    b.color = 3;
    b.value = 13;
    vector<Card> current_hand = {a,b};
    get_best_hand(current_hand);
    return 0;
}