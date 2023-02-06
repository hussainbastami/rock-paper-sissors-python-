import random

# main function for our game
def Game():
    
    #welcome text and game structure
    print('\n\n[r] for rock, [p] for paper, [s] for sissors, [q] for quit')

    #getting input from player
    player_choice = str(input("Please Enter your choice: ")).strip()

    #making a random choice for computer
    computer_choice = random.choice(["r","p","s"])

    #function for comparing player and computer choices
    def compare_options(play_choice, com_choice):
        if computer_choice == com_choice and player_choice == play_choice:
            return True
    
    #function for showing the message
    def show_choices():
        print("Your choice: " + player_choice + "\nMy choice: " + computer_choice)
        
    #win - lost - draw conditions
    if compare_options("r", "s") or compare_options("p", "r") or compare_options("s", "p"):
        print("you won!!!!!!!!!")
        show_choices()
    elif compare_options("r","p") or compare_options("p","s") or compare_options("s","r"):
        print("You lost!!!!!!!!")
        show_choices()
    elif compare_options("r","r") or compare_options("p","p") or compare_options("s","s"):
        print("Draw")
        show_choices()
    #quit condition
    elif player_choice == "q":
        exit()
    #wrong choice condition
    else:
        print("\n\nplease choose one of these options:")
    #re-calling function to start the game from first
    Game()
    
#calling the game function
Game()