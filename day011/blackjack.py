# BLACKJACK
import random
from replit import clear
from blackjack_art import logo

should_continue = True

def sum_score(cards):
  tot = 0
  for card in cards:
      tot += int(card)
  return tot
def blackjack():
  while True:
    clear()
    print(logo)
    print('Welcome to Blackjack!')
    
    # init    
    pl1_score = 0
    pl2_score = 0
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    # random choices
    cpu_choice = random.sample(cards, 2)
    human_choice = random.sample(cards, 2)
    
    pl1_score = sum_score(human_choice)
    pl2_score = sum_score(cpu_choice)
    
    print(f'Your cards: {human_choice}, your score: {pl1_score}')
    print(f'Computer\'s first card: {cpu_choice[0]}')
    
    # draw another card
    draw_another = True
    while draw_another:
      go_again = input('\nType "y" to draw another card, or "n" to pass: ').lower()
      if go_again == 'y':
        human_choice.append(random.choice(cards))
        pl1_score = sum_score(human_choice)
        if pl1_score > 21:
          print(f'Your cards: {human_choice}, your score: {pl1_score}')
          print('\nBust! You lose.\n')
          break
        print(f'Your cards: {human_choice}, your score: {pl1_score}')
      elif go_again == 'n':
        draw_another = False
        if pl1_score > pl2_score:
          fin = 'win'
        else:
          fin = 'lose'
        print(f'\nYou {fin}. Thank you for playing.\n') 
      else:
        print('Type y or n')

    play_again = input("Play again? Type 'y' for yes, 'n' for no: ").lower()
    if play_again == 'n':
      clear()
      print('\nThank you for playing Blackjack. Have a blessed day.')
      break

while True:
    blackjack()
    break