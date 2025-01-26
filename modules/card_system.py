#!/usr/bin/env python3

from operator import attrgetter
import random
import os, os.path
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

path = "./images/resized_images/"
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

    # need to sort it since the images are sorted
    deck = sorted(deck, key=attrgetter("value", "suit"))
    iterator = 0
    for i in deck:
        i.image = images[iterator]
        iterator += 1

    return deck

#deck = make_deck()
#random.shuffle(deck)
#for i in deck:
#    print(i)
