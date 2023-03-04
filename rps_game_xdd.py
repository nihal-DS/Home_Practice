import random


def rps_game():
    player_choice = input("Type 'r' - rock, 'p' - paper, 's' - scissor: ")
    print(f"Player chose : {player_choice}")
    if player_choice not in ['r', 'p', 's']:
        return False

    comp_choice = random.choice(['r', 'p', 's'])

    if player_choice == comp_choice:
        print("Computer chose the same! It's a tie, PlAYYYYY AGANE!!")
        rps_game()

    if player_choice == 'r':
        if comp_choice == 'p':
            print("Computer chose paper, YOU LOSE!")
        if comp_choice == 's':
            print("Computer chose scissor, YOU WIN!")

    if player_choice == 'p':
        if comp_choice == 'r':
            print("Computer chose rock, YOU WIN!")
        if comp_choice == 's':
            print("Computer chose rock, YOU LOSE!")

    if player_choice == 's':
        if comp_choice == 'r':
            print("Computer chose rock, YOU LOSE!")
        if comp_choice == 'p':
            print("Computer chose rock, YOU WIN!")

    rps_game()


rps_game()
