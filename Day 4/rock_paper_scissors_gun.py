#GAME IMAGES
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gun = '''                                                   /////
     _  __)\____________________________________/7_       ()()()
    (//   )))))                                   `\|| ()()()/////
     /   (((((                                      )` ////()
     \   ________ ______________________________/           ////
      ) /#######/ )\  /     )/
     / /##(\)##/ /  \(     //
    / /#######( (\______.ad`
   / /#########) )------``
  / /#########/ /
 / /###(/)###/ /
( (#########/ (
 \____/_______\)
     `
'''
hammer = '''

   T                                    \`.    T
   |    T     .--------------.___________) \   |    T
   !    |     |//////////////|___________[ ]   !  T |
        !     `--------------'           ) (      | !
                                         '-'      !
'''
#img list for selection
game_img = [rock, paper, scissors]

#import random for computer choice
import random

#intro
print('Welcome to Rock, Paper, Scissors')
print('Who will win? The light being created by God himself, or a deterministic machine?')

#human choice
choice = int(input('Choose: Type 0 for Rock, 1 for Paper, 2 for Scissors\n'))

if choice >= 0 and choice < 3:
    print(game_img[choice])
elif choice == 99:
    print(gun)
elif choice == 50:
    print(hammer)
else: #if choice is not rock, paper, or scissors
    print(f'You chose {choice}, which breaks the contract. You lose.')
    exit()

#cpu "choice" using randint()
cpu_choice = random.randint(0, 2)

print(f'Computer "chose" {cpu_choice}')
print(game_img[cpu_choice])
    
#responses based on human's choice
if choice == 99:
    print('***BANG BANG BANG BANG!!!*** the computer is now a heaping pile of sparking scrap metal. You win.')

if choice == 50:
    print('***BAMBAMBAMBAMCRASHBAM!!!*** You savagely bashed the computer with colossal force into a billion pieces. You win.')

#if rock
if choice == 0:
    if cpu_choice == 0:
        print('**CLACK** TIE! Go again!')
    elif cpu_choice == 1:
        print('Really?? You\'re gonna let a computer beat you?\nA MAN MADE PIECE OF METAL????? With a flimsy piece of paper???\nGo again smh...')
    elif cpu_choice == 2:
        print('**KSH KSH KSHKSH** YES!! You obliterated the computer\'s baby scissors with a massive boulder the size of a mountain, lifted as the strength of Allah flows through your ENGORGED veins!!!!! You smashed it with a thunderous boom echoing through the land, leaving a pile of dust. You win.')

#if paper
if choice == 1:
    if cpu_choice == 0:
        print('**WHHHHHUUUU** Your massive net of fiberous interlockings envelops the rock and ejects it into the far edges of the cosmos.\nThe rock is now an irradiated pebble, lost forever, never to be remembered again.\nYou win.')
    elif cpu_choice == 1:
        print('**crinkle** You both chose paper?!\nWhat is this?? an origami class?? This is MAN vs MACHINE!!\nTry again.\nNext time, avoid bringing shame upon your ancestors.')
    elif cpu_choice == 2:
        print('Never bring a piece of paper to a scissor fight...\nYou lose.')

#if scissors
if choice == 2:
    if cpu_choice == 0:
        print('The AI preemptively hired a Pakastani freelancer on UpWork to disassemble your scissors with blinding speed and smash your head in with a rock.\nYou lose.')
    elif cpu_choice == 1:
        print("**SCSCSCSlicceSCSCS** YOUR MASSIVE SCISSOR BLADES eviscerate the AI's paper, sourced from a sweatshop in Beijing, leaving a bunch of microscopic shreds.\nYou win.")
    elif cpu_choice == 2:
        print('The AI\'s algorithm has learned to mirror your attacks perfectly, deflecting every swing.\nTie. Go again.')
