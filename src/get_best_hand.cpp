#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>


using namespace std::chrono;
using namespace std;

struct Card{
    // 1 to 13 (2 to A)
    int value;
    // 0 to 3 (H to D)
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
    vector<Card> color_cards[4];
    // To get the straights
    vector<Card> current_straight = {cards[0]};
    vector<Card> straight;
    // To get straight flushes
    vector<Card> straight_flushes[4];
    straight_flushes[cards[0].color].push_back(cards[0]);
    vector<Card> straight_flush;
    // To get rest of groupings
    vector<vector<Card>> pairs;
    vector<vector<Card>> triples;
    vector<Card> pokers;
    vector<Card> individuals;
    // Temporary variables;
    vector<Card> group = {cards[0]};
    Card last_card = cards[0];
    // Iterate through the sorted cards to extract the posible hands
    for(auto i=cards.begin()+1; i<cards.end(); i++)
	{
        // Search for pairs,triples,etc
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
        // Search for straights
        if ((*i).value - last_card.value == 1){
            current_straight.push_back(*i);
        }else if ((*i).value != last_card.value){
            current_straight.clear();
            current_straight.push_back(*i);
        }
        if (current_straight.size() == 5){
            straight = current_straight;
            current_straight.clear();
        }
        // Search for flushes
        color_cards[(*i).color].push_back(*i);
        // Search for straight flushes
        if (straight_flushes[(*i).color].size() != 0){
            if (straight_flushes[(*i).color][straight_flushes[(*i).color].size()-1].value - (*i).value == 1){
                straight_flushes[(*i).color].push_back(*i);
                if (straight_flushes[(*i).color].size() == 5){
                    straight_flush = straight_flushes[(*i).color];
                }
            }else{
                straight_flushes[(*i).color].clear();
                straight_flushes[(*i).color].push_back(*i);
            }
        }else{
            straight_flushes[(*i).color].push_back(*i);
        }
		last_card = *i;
	}
    // Add the last group
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
    // Check for straight flushes
    if (straight_flush.size() == 0){
        // Iterate through the cards to see if ACES of some color makes a straight flush
        for(auto i=cards.begin(); i<cards.end(); i++)
        {
            if ((*i).value != 13){
                break;
            }else if (straight_flushes[(*i).color].size() == 4 && straight_flushes[(*i).color][0].value == 4){
                straight_flush = straight_flushes[(*i).color];
                straight_flush.push_back(*i);
                break;
            }

        }
    }
    // Create the result hand
    Hand result;
    if (straight_flush.size() != 0){
        if (straight_flush[0].value == 13){
            result.hand_type = "Royal Flush";
        }else{
            result.hand_type = "Straight Flush";
        }
        result.Cards = straight_flush;
        return result;
    }

    if (pokers.size() != 0){
        result.hand_type = "Poker";
        result.Cards = pokers;
        for(auto i=cards.begin(); i<cards.end(); i++){
            if ((*i).value != pokers[0].value){
                result.Cards.push_back(*i);
                break;
            }
        }
        return result;
    }
    
    if (triples.size() > 0 && pairs.size() > 0){
        result.hand_type = "Full House";
        result.Cards = triples[0];
        result.Cards.insert(result.Cards.end(),pairs[0].begin(),pairs[0].end());
        return result;
    }else if(triples.size() == 2){
        result.hand_type = "Full House";
        result.Cards = triples[0];
        result.Cards.insert(result.Cards.end(),triples[1].begin(),triples[1].begin()+2);
        return result;
    }
    // Check flushes
    for (size_t i = 0; i < 4; i++)
    {
        if (color_cards[i].size() >= 5){
            result.hand_type = "Flush";
            result.Cards.insert(result.Cards.end(),color_cards[i].begin(),color_cards[i].begin()+5);
            return result;
        }
    }
    
    // Check if the straight form with an ACE
    if (current_straight.size() == 4 && current_straight[3].value == 1 && cards[0].value == 13){
        straight = current_straight;
        straight.push_back(cards[0]);
    }
    
    if (straight.size() != 0){
        result.hand_type = "Straight";
        result.Cards = straight;
        return result;
    }

    if (triples.size() == 1){
        result.hand_type = "Triples";
        result.Cards = triples[0];
        result.Cards.insert(result.Cards.end(),individuals.begin(),individuals.begin()+2);
        return result;
    }

    if (pairs.size() >= 2){
        result.hand_type = "Double Pairs";
        result.Cards = pairs[0];
        result.Cards.insert(result.Cards.end(),pairs[1].begin(),pairs[1].end());
        result.Cards.push_back(individuals[0]);
        return result;
    }

    if (pairs.size() == 1){
        result.hand_type = "Pairs";
        result.Cards = pairs[0];
        result.Cards.insert(result.Cards.end(),individuals.begin(),individuals.begin()+3);
        return result;
    }
    result.hand_type = "High Card";
    result.Cards.insert(result.Cards.end(),individuals.begin(),individuals.begin()+5);
    return result;
}

Card create_card(int color, int value){
    Card c;
    c.color = color;
    c.value = value;
    return c;
}

int main(){
    vector<Card> current_hand = {create_card(1,2),create_card(2,4),create_card(0,7),create_card(0,2),create_card(3,13),create_card(1,13),create_card(1,12)};
    auto start = high_resolution_clock::now();
    Hand result;
    for (int i = 0; i < 2118760; i++)
    {
        result = get_best_hand(current_hand);
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(stop - start);
    //cout << duration.count()*2118760 << endl;
    cout << duration.count() << endl;
    cout << result.hand_type << "\n";
    print_vector(result.Cards);
    return 0;
}