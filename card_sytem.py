from operator import attrgetter
import os, os.path
import climage
import sys

# Note I will not be adding Joker Cards as they are irrelevant to Poker

suits = {"Clubs" : 0,    #This is to calculate what image im on when looping (4 times through 13)
        "Diamonds" : 1,
        "Hearts" : 2,
        "Spades" : 3}

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

path = "./images/PNG-cards-1.3"
images = [os.path.join(path, file) for file in os.listdir(path)]
#print(images)

# I am considering putting the value of the ace as 14 as it is the most valueble card but it messes up the sorting

class Card(object):

    def __init__(self, value, suit, image=""):
        self.value = value # mainly used for the computer to decide when to bet/fold etc.
        self.suit = suit
        self.face = values[value]
        self.image = image

    def __str__(self):
        if self.value == 1 or  self.value == 8: # check if it starts with a vowel
            return f"an {self.face} of {self.suit}"
        return f"a {self.face} of {self.suit}"

def make_deck():

    deck = [Card(value, suit) for value in  range(1, 14) for suit in suits]

    # need to sort it
    deck = sorted(deck, key=attrgetter("value", "suit"))
    iterator = 0
    for i in deck:
        i.image = images[iterator]
        iterator += 1

    return deck

def show_card(*args):


    img1 = climage.convert(args[0].image, is_unicode=True, width=45)
    img2 = climage.convert(args[1].image, is_unicode=True, width=45)

    print(img1, img2, end="\n")



#checking my work

#cards = 0
#for i in deck:
#    cards += 1
#    print(i, "--" ,i.value)
#print(cards)

sorted_deck = make_deck()
#print(sorted_deck)
#show_card(sorted_deck[1], sorted_deck[2])
for i in sorted_deck:
    print(climage.convert(i.image, is_unicode=True, width=30))

