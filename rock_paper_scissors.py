import random

options = ("rock" , "paper" , "scissors")
player = None
computer = random.choice(options)
running = True # created a variable to keep game running

while running:
    
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("IT's a tie!")
    elif player == "rock"  and computer == "scissors":
        print("You win!")
    elif player == "paper"  and computer == "rock":
        print("You win!")
    elif player == "scissors"  and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
        
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
        # if users input for play again does not equal "y" then set running=false, means stop playing
        
print("Thanks for playing!")