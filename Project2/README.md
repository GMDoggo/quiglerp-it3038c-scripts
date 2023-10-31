# Numpy Blackjack
For Project 1, I created a very simple version of blackjack that utilized random number generation to create card values. In this project, I built upon that project and utilized Numpy arrays to generate a deck of cards full of suits and face values. Furthermore using Numpy arrays allows for cards to be dealt using Array slicing to remove cards from the array once they are dealt.

Clone my repo using the following command or the Desktop application or Download a zip of the Repo.
```python
git clone https://github.com/GMDoggo/quiglerp-it3038c-scripts.git
```
For the following steps I will be using the commands assuming the repo is within C:\
```Powershell
Powershell
PS C:\> C:\quiglerp-it3038c-scripts\Project2\venv\Scripts\Activate.ps1
(venv) PS C:\>
```
Install/Verify that Numpy is Installed
```python
(venv) PS C:\> pip install numpy
Requirement already satisfied: numpy in c:\quiglerp-it3038c-scripts\project2\venv\lib\site-packages (1.26.1)

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\>
```
Navigate to the Project 2 directory and run the Project2.py using Python
```python
(venv) PS C:\> cd C:\quiglerp-it3038c-scripts\Project2\
(venv) PS C:\quiglerp-it3038c-scripts\Project2>
(venv) PS C:\quiglerp-it3038c-scripts\Project2> python .\Project2.py
```
As you can see the game of Blackjack has begun (As deck will be randomized you will see different values)
```python
Player's Hand: [['9', 'Diamonds'], ['2', 'Clubs']] Total: 11
Dealer's Hand: [['Jack', 'Clubs'], ['Queen', 'Diamonds']] Total: 20
Do you want to hit (H) or stand (S)?
```
As the player you are granted the opportunity to Hit or Stand. In my example I am going to type "H" to draw another card since the dealer has 20 and I am at 11.
```python
Do you want to hit (H) or stand (S)? H
Players's Hand: [['9', 'Diamonds'], ['2', 'Clubs'], ['10', 'Spades']] Total: 21
Dealer's Hand: [['Jack', 'Clubs'], ['Queen', 'Diamonds']] Total: 20
Do you want to hit (H) or stand (S)?
```
Since I got a 21 while the Dealer has 20 I am going to stand and I will win!
```python
Players's Hand: [['9', 'Diamonds'], ['2', 'Clubs'], ['10', 'Spades']] Total: 21
Dealer's Hand: [['Jack', 'Clubs'], ['Queen', 'Diamonds']] Total: 20
Do you want to hit (H) or stand (S)? S
Player wins!
Play again y/n?
```
If you would like to play again type "y" to play again and the deck will reshuffle and new hands will be dealt!
```python
Play again y/n?y
Player's Hand: [['Jack', 'Spades'], ['3', 'Spades']] Total: 13
Dealer's Hand: [['7', 'Spades'], ['King', 'Hearts']] Total: 17
Do you want to hit (H) or stand (S)?
```
Once you have played enough type "n" to exit. You then can deactivate and close the Powershell window.
```python
Play again y/n?n
Play again y/n?n
(venv) PS C:\quiglerp-it3038c-scripts\Project2> deactivate
PS C:\quiglerp-it3038c-scripts\Project2>
```
Thanks for playing!


