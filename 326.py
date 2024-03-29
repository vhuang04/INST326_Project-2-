import random 
suits = ["Heart", "Diamond", "Spade","Club"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
card_values = [2,3,4,5,6,7,8,9,10,10,10,10]



print("Suits:",suits)
print("Ranks:", ranks)
print("Card Values:", card_values)

deck_of_cards = []
for suit in suits:
    for rank in ranks:
        card_name = f'{rank}_of_{suit}'
        deck_of_cards.append(card_name)
        print("Deck of Cards:", card_name)
print(len(deck_of_cards))
print(len(set(deck_of_cards)))


random.shuffle(deck_of_cards)
print("Shuffled Deck:", (deck_of_cards))

hearts = []
spades = []
clubs = []
diamonds = []

for card in deck_of_cards:
    if "Heart" in card:
        hearts.append(card)
    elif "Spade" in card:
        spades.append(card)
    elif "Club" in card:
        clubs.append(card)
    else:
        diamonds.append(card)    
        
print(hearts)
print(spades)
print(clubs)
print(diamonds)

print(len(hearts))
print(len(spades))
print(len(clubs))
print(len(diamonds))

deck2 = []
deck2.extend(hearts + spades + clubs + diamonds)
print (deck2)
random.shuffle(deck2)
print(deck2)
print(len(deck2))
print(len(set(deck2)))

my_dict = dict([])
for card in deck2:
    if '2'in card:
        my_dict[card] = 2
    elif '3' in card:
        my_dict[card] = 3 
    elif '4' in card:
        my_dict[card] = 4
    elif '5' in card:
        my_dict[card] = 5
    elif '6' in card:
        my_dict[card] = 6
    elif '7' in card:
        my_dict[card] = 7
    elif '8' in card:
        my_dict[card] = 8
    elif '9' in card:
        my_dict[card] = 9
    else:
        my_dict[card] = 10 
        
print(my_dict)






