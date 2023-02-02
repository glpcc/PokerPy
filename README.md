# PokerPy

A python module writen in C++ for caculating Texas Hold'em poker odds in under a second. The union between python and C++ is done with [pybind11](https://github.com/pybind/pybind11) 

# Installation

# Documentation

## Card Class
```python
class Card:
    def __init__(self, card:str) -> None: ...
    @property
    def value(self) -> str: ...
    @property
    def color(self) -> str: ...
```
The Card class is used to represent a poker card, for the creation of a class you must pass a string with the form *KD* In which the first letter/s represent the value of the card i.e from 2 to A.Then the second letter represents the color of the card it can be passed as *D-H-C-S* or using the unicode characters *♣,♦,♥,♠*.

Internally Card are stored as a struct with two int values, not accesible from the python interface.

### Warning 
At the time no checks for valid values of color and value are done so it is left to the user responsability. With undefined behaviour if done incorrectly.
## Hand Class
```python
class Hand:
    def __init__(self, hand_type: str, Cards: list[Card]) -> None: ...
    @property
    def hand_type(self) -> str: ...
    @property
    def Cards(self) -> list[Card]: ...
```
This is a class to represent a poker Hand with a list of 5 cards representing the 5 chosen cards of the Hand and the Hand_type property, a string representing the type of the Hand. The value of the hand_type can be one of the following,in order of value.
```text
Royal Flush
Straight Flush
Poker
Full House
Flush
Straight
Triples
Double Pairs
Pairs
High Card
```
It is not recommended to create Hand Classes manually unless you want to calculate a specific Hand Heuristic. It should be mainly used as the return type of the *get_best_hand* function.
### Warning 
At the time no checks for valid values of hand_type or the number of hands are done so it is left to the user responsability. With undefined behaviour if done incorrectly.

## Utility Functions 

### get_best_hand
```python
def get_best_hand(cards: list[Card]) -> Hand: ...
```
It gets a list of 7 cards and returns the best possible Hand as a hand_type.

Internally it sorts the cards and perform different checks for different types of hands on a single for loop for performance. It is internally used in the *calculate_hand_frecuencies*.

### Warning 
At the time it isn't checked if the correct number of cards is supplied or if there is any repeated cards. Any thing outside 7 valid,non repeated cards is undefined behaviour.

### calculate_hand_frecuency
```python
def calculate_hand_frecuency(cards: list[list[Card]]) -> list[dict[str,int]]: ...
```
Function that gets a list of players cards, and returns a list with all the hands frecuencies for each player, taking into account the other players hands.
It also calculates the win and draw frecuency of each player, this is shown as the keys "Win" and "Draw" in each players dictionaries.

It is done by iterating for all the possibe combinations of cards and calculating the best hand.

### Warning 
The number of cards per player supplied must be between 2 and 6.And all players should have the same cards. However different players can repeat cards, for example the fold should be shared upon all players.
Anything outside these bounds is UNDEFINED BEHAVIOUR.

### nice_print_frecuencies
```python
def nice_print_frecuencies(frecs: list[dict[str,int]]) -> None: ...
```
Function that gets a the frecuencies of the *calculate_hand_frecuency* function and prints them in a nice table format.

### calculate_hand_heuristic
```python
def calculate_hand_heuristic(hand: Hand) -> int: ...
```
Function that gets a hand and uses bitshifting to calculate a hand value efficienly. It ensures that if a hand is better than another in texas hold'em, this function returns a larger int for the better hand.

This is used internally in the *calculate_hand_frecuency* function to calculate the win,draw chance of every possible combination of cards.

# Limitations 
Supports up to 10 players, and might run slower than a second in old hardware.