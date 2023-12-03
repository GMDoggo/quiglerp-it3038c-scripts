import numpy as np

# Function to create a deck of cards
def create_deck():
    #Using Numpy we create a deck of cards and deal them using array slicing to remove values from the
    #Create deck of cards using numpy array to allow suits and value
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    facevalue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = np.array([(face, suit) for suit in suits for face in facevalue])
    return deck

# Define values for cards using card counting strategy to help train card counting
def card_value(card):
    facevalue, _ = card
    if facevalue in ['2', '3', '4', '5', '6']:
        return 1
    elif facevalue in ['10', 'Jack', 'Queen', 'King', 'Ace']:
        return -1
    else:
        return 0
    
# Adds to the running count
def update_count(hand):
    global count
    for card in hand:
        count += card_value(card)


def blackjack_game():
    global count
    count = 0  # Initialize count here
    bj = True
    cards_remaining = 52  # Total number of cards in the deck initially

    while bj:
        if cards_remaining < 5:  # You can adjust this value to define when to reshuffle
            print("Deck is being reshuffled...")
            cards_remaining = 52
        print("Remaining cards:", cards_remaining)

        deck = create_deck()
        np.random.shuffle(deck)
        cards_remaining -= 4  # Dealing 2 cards to player and 2 cards to dealer
        print("Remaining cards:", cards_remaining)

        # Deal one card to the player
        player_hand = [deck[0]]
        # Deal one card to the dealer
        dealer_hand = [deck[1]]
        # Remove the dealt cards from the deck
        deck = deck[2:]
        # Deal one more card to the player
        player_hand.append(deck[0])
        # Remove the dealt card from the deck
        deck = deck[1:]
        # Deal another card to dealer
        dealer_hand.append(deck[0])
        # Remove the dealt card from the deck
        deck = deck[1:]
        # Update the count for the dealt hands
        update_count(player_hand)
        update_count(dealer_hand)

        def calculate_total(hand):
            #Starts hand value at 0 
            #Start a counter for number of aces in hand       
                total = 0   
                aces = 0    
            #Create a loop for each card in hand and calculate
            #Takes the face value from the card     
                for card in hand:
                    facevalue, _ = card     
                    if facevalue in ['Jack', 'Queen', 'King']:
            #Assign facecards the value of 10            
                        total += 10 
                    elif facevalue == 'Ace':
            #Aces are worth 11 unless you go over 21            
                        total += 11 
            #Add a count for aces in hand            
                        aces += 1 
                    else:
            #Takes integer from any other card            
                        total += int(facevalue)
            #Put a check in for aces being counter as zero
                while total > 21 and aces > 0:
            #If the total is greater than 21 and you have an Ace subtract 10 to count it as 1 
            #Reduce the count of aces by 1       
                    total -= 10 
                    aces -= 1
                return total

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)


        #Print Hands without Numpy elements using tolist to covery to standard list.
        print("Player's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
        print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)

        while True:
            try:
                player_count = int(input("What's the current count? "))
                if player_count == count:
                    print("Correct count!")
                    break
                else:
                    print(f"Incorrect count. The correct count is {count}. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the count.")




        while player_total <= 21 and dealer_total <= 21:
            decision = input("Do you want to hit (H) or stand (S)? ").upper()
            # Deal the player an additional card if they Hit
            if decision == "H":
                player_hand.append(deck[0])
                update_count([deck[0]])  # Update count for the newly dealt card
                player_total = calculate_total(player_hand)
                deck = deck[1:]
                print("Player's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
                if player_total > 21:
                    break
            elif decision == "S":
                break
            else:
                print("Invalid input. Please enter 'H' to hit or 'S' to stand.")

            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)


    # If dealer has less or equal to 17 they have to hit.       
        while dealer_total <= 17:
                dealer_hand.append(deck[0])
                
                dealer_total = calculate_total(dealer_hand)
                update_count(dealer_hand)
                deck = deck[1:]   
                print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)



        # Determine the outcome of the game and print hands
        if player_total > 21:
                print("Player busts. Dealer wins!")
        elif dealer_total > 21:
                print("Dealer busts. Player wins!")
        elif player_total == dealer_total:
                print("It's a push. The game is tied.")
        elif player_total > dealer_total:
                print("Player wins!")
        else:
                print("Dealer wins.")
                
        #Fixed to ensure proper input
        while True:
            play = input("Play again y/n? ").lower()
            if play == "y":
                break
            elif play == "n":
                bj = False
                break
            else:
                print("Invalid input. Please enter 'y' to play again or 'n' to quit.")


blackjack_game()
