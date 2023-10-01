#Guessing Game
print("Guess the Number between 1 and 100")


#Generate a random integer from 1-100
import random

random_number = (random.randint(1,100))

#Start the loop

while True:
    
    #Prompts the user for a guess
    guess = int(input("Enter you guess: "))

    #If statements to determine if guess is higher or lower than the random int
    if guess < random_number:
        print("Your guess is too low")
    elif guess > random_number:
        print("Your guess is too high")
    #Exit the loop if number is correct
    else:
        print("Correct!")
        break
        

