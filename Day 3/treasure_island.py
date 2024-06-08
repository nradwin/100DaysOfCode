print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You are at a crossroads. Do you want to go left or right?")
direction = input("Type 'left' or 'right'\n")
if direction == "left":
          print("You have come to a lake. There is an island in the middle of the lake. Do you want to swim or wait for a boat?")
          action = input("Type 'swim' or 'wait'\n")
          if action == "wait":
                    print('You have come to a house with three doors. One red, one yellow and one blue. Which colour do you choose?')
                    color = input("Type 'red', 'yellow' or 'blue'\n")
                    if color == "red":
                              print(f"You have been burned by fire. Game over.")
                    elif color == "yellow":
                              print(f"You have found the treasure! You win!")
                    elif color == "blue":
                               print(f"You have been eaten by beasts. Game over.")
                    else:
                              print(f"You have chosen a door that doesn't exist. Game over.")
          else: 
                    print("You have been eaten by a megaladon. Game over.")
else:
          print("You have fallen into a hole. Game over.")
