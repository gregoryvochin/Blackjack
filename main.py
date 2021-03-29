import Blackjack

play = "y"

while play == "y":

    Blackjack.deal_cards()
    
    Blackjack.user_blackjack()

    print(f"User total: {Blackjack.user_total()}")
    print(f"Dealer total: {Blackjack.comp_total()}")

    play = input("Would you like to play again? Type 'y' for yes and 'n' for no: ")
    print("\n")

    Blackjack.reset()
    #Blackjack.user_cards = []
    #Blackjack.comp_cards = []
