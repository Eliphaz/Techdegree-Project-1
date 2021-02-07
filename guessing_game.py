"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    num = random.randint(1,10)
    guess = 0
    count = 0
    while guess != num:
      try:
        guess = int(input('please enter a number between 1 and 10:  '))
        if guess <= 10:
          count += 1
        elif guess >= 11:
          print("do you even know how to read")
      except ValueError:
        print('that is not a valid input please enter a integer between 1 and 10')
      if guess == num:
        print('congrats, that is the right number')
        print(f'it took you {count} trys to guess the number')
        if count < 3:
          print ('probably luck...')
        elif count < 5:
          print('good job, I am impressed human')
        elif count < 6:
          print('pretty average for a biological intelligence')
        elif count < 10:
          print('id expect nothing better from a filthy meat based processing unit.')
        elif count > 10:
          print('i can not calculate the probablity that you could fail this badly, i\'m almost impressed.')
        restart = input('would you like to try again (y/n):  ')
        if restart == 'y':
          start_game()
        elif restart == 'n':
          print('have a good day!')
      elif num > guess:
        print('that guess is too low')
      elif num < guess:
        print('that guess is too high')
      

# Kick off the program by calling the start_game function.
print('WELCOME TO THE GUESSING GAME!!!')
print('a standard human can complete this task with 5 or less guesses')
start_game()