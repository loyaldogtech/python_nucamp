import random

pips = random.random()

pips = random.randint(1, 6)
print("You roll the die... it lands with ", pips, " pips showing.")

prizes = ["a car", "a house", "a unicorn", "a donkey", "a zebra"]

prize = random.choice(prizes)   
print("And the winner is: ", prize)

cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
random.shuffle(cards)
print("The card order is: ", cards)
