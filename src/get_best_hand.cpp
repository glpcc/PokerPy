#include <string>
#include <iostream>
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
    Card Cards[5];
};

void print_cards(Card cards[7]){
    for(auto i=0; i<5; i++)
	{
		cout<<cards[i].value << " " << cards[i].color << "\n";
	}
}

Hand get_best_hand(Card cards[7]){
    // Sort the cards
    sort(cards,cards+7,[](Card &a,Card &b){return a.value > b.value;});
    // Divide the cards by color
    Card color_cards[4][7];
    int num_color_cards[4] = {0,0,0,0};
    color_cards[cards[0].color][0] = cards[0];
    num_color_cards[cards[0].color]++;
    // To get the straights
    Card current_straight[5];
    current_straight[0] = cards[0];
    int current_straight_size = 1;
    Card straight[5];
    bool found_straight = false;
    // To get straight flushes
    Card straight_flushes[4][7];
    straight_flushes[cards[0].color][0] = cards[0];
    int straight_flushes_sizes[4] = {0,0,0,0};
    straight_flushes_sizes[cards[0].color] += 1;
    Card straight_flush[5];
    bool found_straight_flush = false;
    // To get rest of groupings
    Card pairs[3][2];
    int num_pairs = 0;
    Card triples[2][3];
    int num_triples = 0;
    Card pokers[4];
    bool found_poker = false;
    Card individuals[7];
    int num_individuals = 0;
    // Temporary variables;
    Card group[4];
    int group_size = 1;
    group[0] = cards[0];
    Card last_card = cards[0];
    // Iterate through the sorted cards to extract the posible hands
    for(auto i=1; i<7; i++)
	{
        // Search for pairs,triples,etc
        if (cards[i].value == last_card.value){
            group[group_size] = cards[i];
            group_size++;
        }else{
            switch (group_size)
            {
            case 1:
                individuals[num_individuals] = cards[i];
                num_individuals++;
                break;
            case 2:
                pairs[num_pairs][0] = group[0];
                pairs[num_pairs][1] = group[1];
                num_pairs++;
                break;
            case 3:
                triples[num_triples][0] = group[0];
                triples[num_triples][1] = group[1];
                triples[num_triples][2] = group[2];
                num_triples++;
                break;
            case 4:
                pokers[0] = group[0];
                pokers[1] = group[1];
                pokers[2] = group[2];
                pokers[3] = group[3];
                found_poker = true;
                break;
            }
            group_size = 1;
            group[0] = cards[i];
        }
        // Search for straights
        if (cards[i].value - last_card.value == 1){
            current_straight[current_straight_size] = cards[i];
            current_straight_size++;
        }else if (cards[i].value != last_card.value){
            current_straight_size = 1;
            current_straight[0] = cards[i];
        }
        if (current_straight_size == 5){
            copy(current_straight,current_straight+5,straight);
            current_straight_size = 0;
            found_straight = true;
        }
        // Search for flushes
        color_cards[cards[i].color][num_color_cards[cards[i].color]] = cards[i];
        num_color_cards[cards[i].color]++;
        // Search for straight flushes
        if (straight_flushes_sizes[cards[i].color] != 0){
            if (straight_flushes[cards[i].color][straight_flushes_sizes[cards[i].color]-1].value - cards[i].value == 1){
                straight_flushes[cards[i].color][straight_flushes_sizes[cards[i].color]] = cards[i];
                straight_flushes_sizes[cards[i].color]++;
                if (straight_flushes_sizes[cards[i].color] == 5){
                    copy(straight_flushes[cards[i].color],straight_flushes[cards[i].color]+5,straight_flush);
                    found_straight_flush = true;
                    straight_flushes_sizes[cards[i].color] = 0;
                }
            }else{
                straight_flushes_sizes[cards[i].color] = 1;
                straight_flushes[cards[i].color][0] = cards[i];
            }
        }else{
            straight_flushes[cards[i].color][0] = cards[i];
        }
		last_card = cards[i];
	}
    // Add the last group
    switch (group_size)
    {
    case 1:
        individuals[num_individuals] = group[0];
        num_individuals++;
        break;
    case 2:
        pairs[num_pairs][0] = group[0];
        pairs[num_pairs][1] = group[1];
        num_pairs++;
        break;
    case 3:
        triples[num_triples][0] = group[0];
        triples[num_triples][1] = group[1];
        triples[num_triples][2] = group[2];
        break;
    case 4:
        pokers[0] = group[0];
        pokers[1] = group[1];
        pokers[2] = group[2];
        pokers[3] = group[3];
        break;
    }
    // Check for straight flushes
    if (!found_straight_flush){
        // Iterate through the cards to see if ACES of some color makes a straight flush
        for(int i=0; i<7; i++)
        {
            if (cards[i].value != 13){
                break;
            }else if (straight_flushes_sizes[cards[i].color] == 4 && straight_flushes[cards[i].color][0].value == 4){
                copy(straight_flushes[cards[i].color],straight_flushes[cards[i].color]+4,straight_flush);
                straight_flush[4] = cards[i];
                found_straight_flush = true;
                break;
            }

        }
    }
    // Create the result hand
    Hand result;
    if (found_straight_flush){
        if (straight_flush[0].value == 13){
            result.hand_type = "Royal Flush";
        }else{
            result.hand_type = "Straight Flush";
        }
        copy(straight_flush,straight_flush+5,result.Cards);
        return result;
    }

    if (found_poker){
        result.hand_type = "Poker";
        copy(pokers,pokers+4,result.Cards);
        for(int i=0; i<7; i++){
            if (cards[i].value != pokers[0].value){
                result.Cards[4] = cards[i];
                break;
            }
        }
        return result;
    }
    
    if (num_triples > 0 && num_pairs > 0){
        result.hand_type = "Full House";
        copy(triples[0],triples[0]+3,result.Cards);
        result.Cards[3] = pairs[0][0];
        result.Cards[4] = pairs[0][1];
        return result;
    }else if(num_triples == 2){
        result.hand_type = "Full House";
        copy(triples[0],triples[0]+3,result.Cards);
        result.Cards[3] = triples[1][0];
        result.Cards[4] = triples[1][1];
        return result;
    }
    // Check flushes
    for (size_t i = 0; i < 4; i++)
    {
        if (num_color_cards[i] >= 5){
            result.hand_type = "Flush";
            copy(color_cards[i],color_cards[i]+5,result.Cards);
            return result;
        }
    }
    
    // Check if the straight form with an ACE
    if (!found_straight && current_straight_size == 4 && current_straight[3].value == 1 && cards[0].value == 13){
        copy(current_straight,current_straight+4,straight);
        found_straight = true;
        straight[4] = cards[0];
    }
    
    if (found_straight){
        result.hand_type = "Straight";
        copy(straight,straight+5,result.Cards);
        return result;
    }

    if (num_triples == 1){
        result.hand_type = "Triples";
        copy(triples[0],triples[0]+3,result.Cards);
        result.Cards[3] = individuals[0];
        result.Cards[4] = individuals[1];
        return result;
    }

    if (num_pairs >= 2){
        result.hand_type = "Double Pairs";
        result.Cards[0] = pairs[0][0];
        result.Cards[1] = pairs[0][1];
        result.Cards[2] = pairs[1][0];
        result.Cards[3] = pairs[1][1];
        result.Cards[4] = individuals[0];
        return result;
    }

    if (num_pairs == 1){
        result.hand_type = "Pairs";
        result.Cards[0] = pairs[0][0];
        result.Cards[1] = pairs[0][1];
        result.Cards[2] = individuals[0];
        result.Cards[3] = individuals[1];
        result.Cards[4] = individuals[2];
        return result;
    }
    result.hand_type = "High Card";
    copy(individuals,individuals+5,result.Cards);
    return result;
}

Card create_card(int color, int value){
    Card c;
    c.color = color;
    c.value = value;
    return c;
}

int main(){
    Card current_hand[7] = {create_card(1,12),create_card(2,4),create_card(1,10),create_card(1,11),create_card(1,9),create_card(2,7),create_card(1,13)};
    string posible_hand_types[12] = {"Straight Flush","Royal Flush","Poker","Full House","Flush","Straight","Triples","Double Pairs","Pairs","High Card"};
    auto start = high_resolution_clock::now();
    Hand result;
    // Iterate over the combinations
    // 2118760
    // result = get_best_hand(current_hand);
    for (int i = 0; i < 2118760; i++)
    {
        result = get_best_hand(current_hand);
    }
    cout << "Holaaa" << endl;
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<nanoseconds>(stop - start);
    //cout << duration.count()*2118760 << endl;
    cout << duration.count() << endl;
    cout << result.hand_type << endl;
    print_cards(result.Cards);
    return 0;
}