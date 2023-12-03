# Numpy Blackjack
### For my Final, I made the following changes to my Project 2.

- Separation of Deck Creation and Main Game Logic into Separate Functions.
- Reshuffling of the deck at the beginning of play and when the remaining cards fall below 5.
- Altered main loop for better game flow.
- Improved input validation for a smoother user experience.
- Added Splitting functionality for the game.
- Included a Card Counting Helper that quizzes the player on the current deck count.
  - Cards 2 to 6 increment the count by +1.
  - Cards 7 to 9 maintain the count at 0.
  - 10s and Aces decrement the count by -1.

#### Basic Card Counting Strategy

  - Cards 2 to 6 increment the count by +1.
  - Cards 7 to 9 maintain the count at 0.
  - 10s and Aces decrement the count by -1.
  - When the Count is High such as +5 that means the deck contains more face cards, making it easier to land a Win against the dealer

#### Clone my repo using the following command or the Desktop application or Download a zip of the Repo.
```python
git clone https://github.com/GMDoggo/quiglerp-it3038c-scripts.git
```
#### For the following steps I will be using the commands assuming the repo is within C:\
```Powershell
Powershell
PS C:\> PS C:\> & 'C:\quiglerp-it3038c-scripts\Final Project\venv\Scripts\Activate.ps1'
(venv) PS C:\>
```
#### Install/Verify that Numpy is Installed
```python
(venv) PS C:\> pip install numpy
Requirement already satisfied: numpy in c:\quiglerp-it3038c-scripts\project2\venv\lib\site-packages (1.26.1)

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\>
```
#### Navigate to the Project 2 directory and run the Project2.py using Python
```python
(venv) PS C:\> cd 'C:\quiglerp-it3038c-scripts\Final Project\'
(venv) PS C:\quiglerp-it3038c-scripts\Final Project> python .\Final.py
```
#### As you can see the game of Blackjack has begun, The deck has been shuffled and will count the remaining cards. As the player you have to keep track of the running count to improve odd's of winning. Since 2-6 is +1 and Face Cards or an Ace is -1. The current count will still be 1.
```python
Remaining cards: 52
Remaining cards: 48
Player's Hand: [['5', 'Spades'], ['9', 'Clubs']] Total: 14
Dealer's Hand: [['6', 'Diamonds'], ['10', 'Clubs']] Total: 16
What's the current count? 1
Correct count!
```
#### As the player you are granted the opportunity to Hit or Stand. In my example I am going to type "H" to draw another card since the dealer has 16 and I have 14. I sadly draw a Jack and bust. Since I was dealt a Jack the new count is -1
```python
Do you want to hit (H) or stand (S)? H
Player's Hand: [['5', 'Spades'], ['9', 'Clubs'], ['Jack', 'Diamonds']] Total: 24
Dealer's Hand: [['6', 'Diamonds'], ['10', 'Clubs']] Total: 16
Player busts. Dealer wins!
Play again y/n?
```
#### You may now choose to play again and the count will continue to be tracked until the deck is reshuffled.
```python
Play again y/n? y
Remaining cards: 48
Remaining cards: 44
Player's Hand: [['8', 'Diamonds'], ['10', 'Spades']] Total: 18
Dealer's Hand: [['4', 'Diamonds'], ['6', 'Diamonds']] Total: 10
What's the current count?
```
#### Once you have played enough type "n" to exit. You then can deactivate and close the Powershell window.
```python
Dealer busts. Player wins!
Play again y/n? n
(venv) PS C:\quiglerp-it3038c-scripts\Final Project>
(venv) PS C:\quiglerp-it3038c-scripts\Final Project> deactivate
PS C:\quiglerp-it3038c-scripts\Final Project>
```
Thanks for playing!


