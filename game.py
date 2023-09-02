# Python | Check if a Substring is Present in a Given String
#
#
# main_string = "Hello, how are you?"
# substring = ""
#
# if substring in main_string and substring != "":
#     print("Substring found!")
# else:
#     print("Substring not found.")

# rock , paper and scissor game

import random


print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice"))

    while choice > 3 or choice < 1:
        choice = int(input('enter a valid choice '))
    result = ""

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    # we need to check of a draw

    if choice == comp_choice:
        print('its a draw', end="")
        result = "Draw"
    # condition for winning

    if choice == 1 and comp_choice == 2:
        print('paper wins =>', end="")
        result = 'paper'
    elif choice == 1 and comp_choice == 2:
        print('paper wins =>', end="")
        result = 'Paper'

    if choice == 1 and comp_choice == 3:
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif choice == 3 and comp_choice == 1:
        print('Rock wins =>\n', end="")
        result = 'rocK'

    if choice == 2 and comp_choice == 3:
        print('Scissors wins =>', end="")
        result = 'scissor'
    elif choice == 3 and comp_choice == 2:
        print('Scissors wins =>', end="")
        result = 'Rock'

    # Printing either user or computer wins or draw

    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input().lower
    if ans == 'n':
        break

    print("thanks for playing")

