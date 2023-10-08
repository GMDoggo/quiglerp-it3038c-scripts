import random

# Loops if bj = true
bj = True
while bj == True:
    # Generate 4 randomint for the 4 starting cards
    card1 = random.randint(1, 11)
    card2 = random.randint(1, 11)
    card3 = random.randint(1, 11)
    card4 = random.randint(1, 11) 

    # Simple total calculation
    playertotal = card1 + card3
    dealertotal = card2 + card4
    print("Dealer Has", dealertotal)
    print("Player Has", playertotal)

    # While either the dealer or player has less than 21 prompt user to hit or stand
    while playertotal <= 21 and dealertotal <= 21:
        decision = input("Do you want to hit (H) or stand (S)? ").upper()
        # Deal the player an additional card if they Hit
        if decision == "H":
            card5 = random.randint(1, 11)
            playertotal += card5
            print("Player drew a card new total is:", playertotal)
        # Stand exits the loop
        elif decision == "S":
            break
        # Ensure proper input
        else:
            print("Invalid input. Please enter 'H' to hit or 'S' to stand.")
    # If dealer has less or equal to 17 they have to hit.       
    while dealertotal <= 17:
        card6 = random.randint(1, 11)
        dealertotal += card6
        print("Dealer drew a card. New total is:", dealertotal)

    # Display the final totals
    print("Final Dealer Total:", dealertotal)
    print("Final Player Total:", playertotal)

    # If statements to determine who won
    if playertotal > 21:
        print("Player has busted! Dealer wins.")
    elif dealertotal > 21:
        print("Dealer has busted! Player wins.")
    elif playertotal > dealertotal:
        print("Player wins!")
    elif playertotal < dealertotal:
        print("Dealer wins!")
    else:
        print("It's a Push")
# Prompt user to play again if y repeat.
    play = input("Play again y/n?")
    if play =="y":
        bj = True
    else:
        bj = False   
