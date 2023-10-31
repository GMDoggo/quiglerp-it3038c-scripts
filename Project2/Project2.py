import numpy as np

# Loops if bj = true
bj = True
while bj == True:
    #Using Numpy we create a deck of cards and deal them using array slicing to remove values from the
    #Create deck of cards using numpy array to allow suits and value
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    facevalue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = np.array([(face, suit) for suit in suits for face in facevalue])

    # Shuffle the deck
    np.random.shuffle(deck)
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



    # While either the dealer or player has less than 21 prompt user to hit or stand
    while player_total <= 21 and dealer_total <= 21:
        decision = input("Do you want to hit (H) or stand (S)? ").upper()
        # Deal the player an additional card if they Hit
        if decision == "H":
            player_hand.append(deck[0])
            player_total = calculate_total(player_hand)
            deck = deck[1:]
        # Stand exits the loop
        elif decision == "S":
            break
        # Ensure proper input
        else:
            print("Invalid input. Please enter 'H' to hit or 'S' to stand.")
            # Print the new values of the player's and dealer's hands
        print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
        print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)


# If dealer has less or equal to 17 they have to hit.       
    while dealer_total <= 17:
            dealer_hand.append(deck[0])
            dealer_total = calculate_total(dealer_hand)
            deck = deck[1:]   




    # Determine the outcome of the game and print hands
    if player_total > 21:
            print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("Player busts. Dealer wins!")
    elif dealer_total > 21:
            print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("Dealer busts. Player wins!")
    elif player_total == dealer_total:
            print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("It's a push. The game is tied.")
    elif player_total > dealer_total:
            print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("Player wins!")
    else:
            print("Players's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("Dealer wins.")


# Prompt user to play again if y repeat.
    play = input("Play again y/n?")
    if play =="y":
        bj = True
    else:
        bj = False   