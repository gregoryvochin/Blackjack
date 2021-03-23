import random

#plays = {hit: hit(), stand: stand()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
user_total = 0

comp_cards = []
comp_total = 0

def deal_cards():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))

    print(f"You were dealt {user_cards}")
    print(f"The computer was dealt [?, {comp_cards[1]}]")

def hit():
    user_cards.append(random.choice(cards))

def stand():
    print("You end your turn!")

def user_total():
    user_total = sum(user_cards)
    return user_total

def comp_total():
    comp_total = sum(comp_cards)
    return comp_total

deal_cards()

def blackjack(user_total = user_total, comp_total = comp_total):
    winOrLose = None
    hitOrStand = None
    
    user_total = user_total()
    comp_total = comp_total()
    
    if user_total == 21:
        print("Blackjack!")
        if comp_total == 21:
            print("Push!")
            return winOrLose
        else:
            print("You win!")
            winOrLose = True
            return winOrLose

    elif user_total > 21:
        if 11 in user_cards:
            for card in range(0, len(user_cards)):
                if user_cards[card] == 11:
                    user_cards[card] = 1
                    print(f"You went over 21, but had an Ace! Your new cards are {user_cards}")
                    blackjack()
        else:
            print(f"Bust! Your total ({user_total}) went over 21!")
            winOrLose = False
            return winOrLose

    else:
        
        hitOrStand = input("Enter 'hit' to get a card, or 'stand' to keep what you have and let the dealer play.")
        hitOrStand = hitOrStand.lower()
        if hitOrStand == "hit":
            hit()
            print(user_cards)
            blackjack()

blackjack()

print(user_total())
print(comp_total())
