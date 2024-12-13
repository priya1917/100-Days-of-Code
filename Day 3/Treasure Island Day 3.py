print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print('You\'re at a cross road. Where do you want to go?Type "left" or "right"\n')
choice1 = input()
print(choice1)
if choice1 == 'left':
    choice2= input(print('You have arrived at a river type "swim" if you want ot swim across or type "wait" to wait.\n')).lower()
    if choice2 == 'wait':
        choice3 = input('You see three doors in front "Red","Blue" and "Yellow". Which one do you want to enter?\n').lower
        if choice3 == "yellow":
            print("You win the game !!")
        elif choice3 == "red":
            print("Burned by fire. Game Over !!")
        elif choice3 == "blue":
            print("Eaten by a beast. Game Over !!")
        else:
            print("Game Over !!")
    else:
        print("You got attacked by an angry fish. Game over !!")
else:
    print("You fell into a hole.Game over !!!")

