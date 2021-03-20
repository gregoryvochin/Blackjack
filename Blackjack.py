import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []

comp_cards = []

def deal_cards():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))

def hit():
    user_cards.append(random.choice(cards))

deal_cards()
print(user_cards)
print(comp_cards)
hit()

print(user_cards)
print(comp_cards)
