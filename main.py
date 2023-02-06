import random


def Game():
    print('\n\n[r] for rock, [p] for paper, [s] for sissors, [q] for quit')

    player_choice = str(input("Please Enter your choice: ")).strip()

    computer_choice = random.choice(["r","p","s"])

    def compare_options(play_choice, com_choice):
        if computer_choice == com_choice and player_choice == play_choice:
            return True
        
    def show_choices():
        print("Your choice: " + player_choice + "\nMy choice: " + computer_choice)
        
    if compare_options("r", "s") or compare_options("p", "r") or compare_options("s", "p"):
        print("you won!!!!!!!!!")
        show_choices()
    elif compare_options("r","p") or compare_options("p","s") or compare_options("s","r"):
        print("You lost!!!!!!!!")
        show_choices()
    elif compare_options("r","r") or compare_options("p","p") or compare_options("s","s"):
        print("Draw")
        show_choices()
    elif player_choice == "q":
        exit()
    else:
        print("\n\nplease choose one of these options:")
    
    Game()
    
    
Game()