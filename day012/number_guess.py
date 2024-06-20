# Number Guessing Game
from numberguess_art import logo
import random
print(logo)

cpu_choice = random.choice(range(101))

def val_comp(cpu_choice):
  while True:
    print('Welcome to the Number Guessing Game!')
    diff = input('Choose difficulty: type normal or hard: ')
    if diff == 'normal':
      tries = 10
      break
    elif diff == 'hard':
      tries = 5
      break
    else:
      print('Type "normal" or "hard".')
  
  while tries > 0:   
    print(f'You have {tries} attempts remaining to guess the number.')
    
    valid_input = False
    while not valid_input:
        user_choice = input('Enter your guess (between 0 and 100): ')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if 0 <= user_choice <= 100:
                valid_input = True
            else:
                print('Enter a number between 0 and 100.')
        else:
            print('Enter a number between 0 and 100.')
    
    if user_choice == cpu_choice:
      print(f'You got it! The number was {cpu_choice}.')
      break
    elif user_choice > cpu_choice:
      print('Too high.')
    elif user_choice < cpu_choice:
      print('Too low.')
    else:
      print("Type a number between 0 and 100.")

    tries -= 1
    if tries == 0:
      print("You\'ve run out of guesses. RIP.")

val_comp(cpu_choice)