from operator import attrgetter

# Note I will not be adding Joker Cards as they are irrelevant to Poker

suits = ("hearts", "diamonds", "clubs", "spades") # tuples are more efficient than lists according to my lecturer
values = { 1 : "Ace",
           2 : "Two",
           3 : "Three",
           4 : "Four",
           5 : "Five",
           6 : "Six",
           7 : "Seven",
           8 : "Eight",
           9 : "Nine",
           10 : "Ten",
           11 : "Jack",
           12 : "Queen",
           13 : "King"}

# I am considering putting the value of the ace as 14 as it is the most valueble card but it messes up the sorting

class Card(object):

    def __init__(self, value, suit):
        self.value = value # mainly used for the computer to decide when to bet/fold etc.
        self.suit = suit
        self.face = values[value]

    def __str__(self):
        if self.value == 1 or  self.value == 8: # check if it starts with a vowel
            return f"This is an {self.face} of {self.suit}"
        return f"This is a {self.face} of {self.suit}"

def make_deck(sort_by=1):

    deck = {Card(value, suit) for value in  range(1, 14) for suit in suits}
    # need to sort it

    if 2 < (sort_by // 1) < 1: # Rounds 1.xx and 2.xx to 1 and 2
        return "Invalid Option, Try Again"
    elif sort_by == 1: # This will be the values option
        return sorted(deck, key=attrgetter("value", "suit"))
    else: # This will be the suits option --> 2
        return sorted(deck, key=attrgetter("suit", "value"))


#checking my work

#cards = 0
#for i in deck:
#    cards += 1
#    print(i, "--" ,i.value)
#print(cards)

#sorted_deck = make_deck()
#for i in sorted_deck:
#    print(i)

