import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
user_total = 0

comp_cards = []
comp_total = 0

def deal_cards():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))

def hit():
    user_cards.append(random.choice(cards))

def user_total():
    user_total = sum(user_cards)
    return user_total

def comp_total():
    comp_total = sum(comp_cards)
    return comp_total

deal_cards()

if user_total() > 21:
    print(f"Your total is over 21 with {user_total}. Bust!")

else:
    print(user_total())
    
print(comp_total())
