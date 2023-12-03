import numpy as np

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    facevalue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = np.array([(face, suit) for suit in suits for face in facevalue])
    return deck

def blackjack_game():
    bj = True
    cards_remaining = 52  # Total number of cards in the deck initially

    while bj:
        if cards_remaining < 15:  # You can adjust this value to define when to reshuffle
            print("Deck is being reshuffled...")
            cards_remaining = 52
            print("Remaining cards:", cards_remaining)

        deck = create_deck()
        np.random.shuffle(deck)
        cards_remaining -= 4  # Dealing 2 cards to player and 2 cards to dealer
        print("Remaining cards:", cards_remaining)

        player_hand = [deck[0]]
        dealer_hand = [deck[1]]
        deck = deck[2:]

        player_hand.append(deck[0])
        deck = deck[1:]
        dealer_hand.append(deck[0])
        deck = deck[1:]

        def calculate_total(hand):
            total = 0
            aces = 0
            for card in hand:
                facevalue, _ = card
                if facevalue in ['Jack', 'Queen', 'King']:
                    total += 10
                elif facevalue == 'Ace':
                    total += 11
                    aces += 1
                else:
                    total += int(facevalue)
            while total > 21 and aces > 0:
                total -= 10
                aces -= 1
            return total

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        print("Player's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
        print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)

        while player_total <= 21 and dealer_total <= 21:
            decision = input("Do you want to hit (H) or stand (S)? ").upper()
            if decision == "H":
                player_hand.append(deck[0])
                player_total = calculate_total(player_hand)
                deck = deck[1:]
                cards_remaining -= 1
                print("Remaining cards:", cards_remaining)
            elif decision == "S":
                break
            else:
                print("Invalid input. Please enter 'H' to hit or 'S' to stand.")
            print("Player's Hand:", [card.tolist() for card in player_hand], "Total:", player_total)
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)

        while dealer_total <= 17:
            dealer_hand.append(deck[0])
            dealer_total = calculate_total(dealer_hand)
            deck = deck[1:]
            cards_remaining -= 1
            print("Dealer's Hand:", [card.tolist() for card in dealer_hand], "Total:", dealer_total)
            print("Remaining cards:", cards_remaining)

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

        play = input("Play again y/n? ")
        if play != "y":
            bj = False

blackjack_game()
