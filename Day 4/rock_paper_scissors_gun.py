# GAME IMAGES
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
# img list for selection
game_img = [rock, paper, scissors]
game_choices = ['rock', 'paper', 'scissors', 'HAMMER', 'GUN']

# import random for computer choice
import random

# intro
print('''
                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \  =  /
                 |\___/|                                        
        ___ ____/:     :\____ ___                                              ooooooooooooooooooooooooooooooooooooo
      .'   `.-===-\   /-===-.`   '.                                            8                                .d88
     /      .-"""""-.-"""""-.      \                                           8  oooooooooooooooooooooooooooood8888
    /'             =:=             '\.                                         8  8888888888888888888888888P"   8888    oooooooooooooooo
  .'  ' .:    o   -=:=-   o    :. '  `.                    //                  8  8888888888888888888888P"      8888    8              8
  (.'   /'. '-.....-'-.....-' .'\   '.)          MAN    VERSUS    MACHINE      8  8888888888888888888P"         8888    8             d8
  /' ._/   ".     --:--     ."   \_. '\.                 //                    8  8888888888888P"               8888    8           d888
 |  .'|      ".  ---:---  ."      |'.  |                                       8  8888888888P"                  8888    8          d8888
 |  : |       |  ---:---  |       | :  |                                       8  8888888P"                     8888    8         d88888
  \ : |       |_____._____|       | : /                                        8  8888P"                        8888    8        d888888
  /   (       |----|------|       )   \                                        8  8888oooooooooooooooooooooocgmm8888    8       d8888888
 /... .|      |    |      |      |. ...\                                       8 .od88888888888888888888888888888888    8      d88888888
|::::/'' jgs /     |       \     ''\::::|                                      8888888888888888888888888888888888888    8     d888888888
'""""       /'    .L_      `\       """"'                                                                               8    d8888888888
           /'-.,__/` `\__..-'\                                                    ooooooooooooooooooooooooooooooo       8   d88888888888
          ;      /     \      ;                                                  d                       ...oood8b      8  d888888888888
          :     /       \     |                                                 d              ...oood888888888888b     8 d8888888888888
          |    /         \.   |                                                d     ...oood88888888888888888888888b    8d88888888888888
          |`../           |  ,/                                               dood8888888888888888888888888888888888b
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___)
           |==|
           \__/                                                                 
''')
print('Welcome to Rock, Paper, Scissors! MAN VERSUS MACHINE')
print('Who will win? You, the light being created by God himself, or a deterministic machine?')

#init scores
human_score = 0
cpu_score = 0
first_round = True

# round dialogue
while human_score < 2 and cpu_score < 2:
    if first_round:
        user_msg = '\nType to choose:\n'
    elif human_score and cpu_score == 0:
        user_msg = '\nGo again:\n'   
    elif (human_score ^ cpu_score == 0):
        user_msg = '\nGo again, you got this:\n'
    elif (human_score and cpu_score == 1):
        user_msg = '\nFinal round, the future of humanity hinges on you\n'
    # scoreboard
    print(f'\nSCORE (Best 2-OUT-OF-3)\nYou: {human_score}\nCPU: {cpu_score}')

    # human choice
    choice = int(input(user_msg + '0 for Rock\n1 for Paper\n2 for Scissors\n'))
    
    if choice <= 2:
        print('\nYou chose ' + game_choices[choice])
    elif choice == 99:
        print('\nYou pulled the GLOCK')
    elif choice == 50:
        print('\nYou chose $5 hammer attack')

    if choice >= 0 and choice < 3:
        print(game_img[choice])
    elif choice == 99:
        print(gun)
    elif choice == 50:
        print(hammer)
    else: #if choice is not rock, paper, or scissors
        print(f'You chose {choice}, which breaks the contract. You lose.')
        exit()

    # cpu "choice" using randint()
    cpu_choice = random.randint(0, 2)
    cpu_dialogue = game_choices[cpu_choice]

    print(f'Computer "chose" {cpu_dialogue}')
    print(game_img[cpu_choice])
    
    # responses based on human's choice
    if choice == 99:
        print('***BANG BANG BANG BANG!!!*** the computer is now a heaping pile of sparking scrap metal. You win.')
        human_score += 1

    if choice == 50:
        print('***BAMBAMBAMBAMCRASHBAM!!!*** You savagely bashed the computer with colossal force into a billion pieces. You win.')
        human_score += 1

    # if rock
    if choice == 0:
        if cpu_choice == 0:
            print('**CLACK** TIE! Go again!')
        elif cpu_choice == 1:
            print('Really?? You\'re gonna let a computer beat you?\nA MAN MADE PIECE OF METAL????? With a flimsy piece of paper???\nGo again smh...')
            cpu_score += 1
        elif cpu_choice == 2:
            print('**KSH KSH KSHKSH** YES!! You obliterated the computer\'s baby scissors with a massive boulder the size of a mountain, lifted as the strength of Allah flows through your ENGORGED veins!!!!! You smashed it with a thunderous boom echoing through the land, leaving a pile of dust. You win.')
            human_score += 1
    # if paper
    if choice == 1:
        if cpu_choice == 0:
            print('**WHHHHHUUUU** Your massive net of fiberous interlockings envelops the rock and ejects it into the far edges of the cosmos.\nThe rock is now an irradiated pebble, lost forever, never to be remembered again.\nYou win.')
            human_score += 1
        elif cpu_choice == 1:
            print('**crinkle** You both chose paper?!\nWhat is this?? an origami class?? This is MAN vs MACHINE!!\nTie. Go again.\nNext time, avoid bringing shame upon your ancestors.')
        elif cpu_choice == 2:
            print('Never bring a piece of paper to a scissor fight...\nYou lose.')
            cpu_score += 1

    # if scissors
    if choice == 2:
        if cpu_choice == 0:
            print('The AI preemptively hired a Pakastani freelancer on UpWork to disassemble your scissors with blinding speed and smash your head in with a rock.\nYou lose.')
            cpu_score += 1
        elif cpu_choice == 1:
            print("**SCSCSCSlicceSCSCS** YOUR MASSIVE SCISSOR BLADES eviscerate the AI's paper, sourced from a sweatshop in Beijing, leaving a bunch of microscopic shreds.\nYou win.")
            human_score += 1
        elif cpu_choice == 2:
            print('The AI\'s algorithm has learned to mirror your attacks perfectly, deflecting every swing.\nTie. Go again.')
    
    first_round = False # next round

# announce winner
if human_score > cpu_score:
    print('\nYou defeated the AI with sheer momentum and strength, allowing humans to prosper for eons to come...\n')
else:
    print('\nThe AI will now take over, you are f\'ed...\n')
