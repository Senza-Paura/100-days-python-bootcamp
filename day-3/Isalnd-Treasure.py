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

choice1 = input('you\'ve come to an morrocan island. you see two house. what one you gonna chooose "left" or "right" house ? \n').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to choose one trasnporttation way . type "moto" if you want the motorcycle or type "car" if you want the car \n').lower()
    if choice2 == "car":
        choice3 = input("you arrive to the house. ther is 3 door One red ,  blue and yellow. what door you gonna choose ? \n").lower()
        if choice3 == "red":
            print("you choose the fire. GAME OVER")
        elif choice3 == "yellow":
            print("you find the treasure ! YOU WIN!")
        elif choice3 == "blue":
            print("you choose the frozen door ! you lose ya loser ")
        else:
            print("you choose a door that doesn't exist ! you lose")
    else:
        print("you lose ! GAME OVEEER")
else :
    print("GAME OVER")
