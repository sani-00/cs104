import random

win = 0
tie = 0
lose = 0

player = input("Enter your move (rock, paper, scissors): ")
while player != "q":


    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if player == "rock":
        if computer == "rock":
            print("It's a tie!")
            tie += 1
        elif computer == "paper":
            print("You lose!")
            lose += 1
        elif computer == "scissors":
            print("You win!") 
            win += 1  
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            win += 1
        elif computer == "paper":
            print("It's a tie!")
            tie += 1
        elif computer == "scissors":
            print("You lose!")   
            lose += 1    
    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
            lose += 1
        elif computer == "paper":
            print("You win!")
            win += 1
        elif computer == "scissors":
            print("It's a tie!")
            tie += 1
    else:
        print("Invalid move. Please choose rock, paper, or scissors.")    
    player = input("Enter your move (rock, paper, scissors): ")

print("win:",win)
print("tie:",tie)
print("lose:",lose)