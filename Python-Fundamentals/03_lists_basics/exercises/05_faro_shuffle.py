# First way
deck = input().split()
n_shuffles = int(input())

for shuffle in range(n_shuffles):
    half_of_deck = len(deck) // 2
    left_deck = []
    right_deck = []
    shuffled_deck = []

    for i in range(1, half_of_deck):
        left_deck.append(deck[i])

    for i in range(half_of_deck, len(deck) - 1):
        right_deck.append(deck[i])

    for i in range(len(left_deck)):
        shuffled_deck.append(right_deck[i])
        shuffled_deck.append(left_deck[i])

    shuffled_deck.insert(0, deck[0])
    shuffled_deck.append(deck[-1])
    deck = shuffled_deck.copy()

print(deck)


# Alternative way
cards = input().split()
n_shuffles = int(input())

half_deck = len(cards) // 2
left_deck = cards[1:half_deck]
right_deck = cards[half_deck:len(cards) - 1]

for shuffle in range(n_shuffles):
    shuffled_deck = []
    for i in range(len(left_deck)):
        shuffled_deck.append(right_deck[i])
        shuffled_deck.append(left_deck[i])

    left_deck = shuffled_deck[0:half_deck - 1]
    right_deck = shuffled_deck[half_deck - 1:len(shuffled_deck)]

shuffled_deck.insert(0, cards[0])
shuffled_deck.append(cards[-1])

print(shuffled_deck)


# Another one
starting_deck = input().split()
shuffles = int(input())

top_card = starting_deck[0]
bottom_card = starting_deck[-1]
half_deck = len(starting_deck) // 2
sorted_deck = []

for shuffle in range(shuffles):
    left_deck = starting_deck[1:half_deck]
    right_deck = starting_deck[half_deck:-1]

    for i in range(half_deck - 1):
        sorted_deck.append(right_deck[i])
        sorted_deck.append(left_deck[i])

    starting_deck = sorted_deck
    starting_deck.insert(0, top_card)
    starting_deck.append(bottom_card)
    sorted_deck = []

print(starting_deck)
