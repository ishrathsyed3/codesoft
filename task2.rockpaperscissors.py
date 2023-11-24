'''create a User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback '''

import random

def userchoice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(userchoice, comp_choice):
    if userchoice == comp_choice:
        return "It's a tie!"
    elif (
        (userchoice == 'rock' and comp_choice == 'scissors') or
        (userchoice == 'scissors' and comp_choice == 'paper') or
        (userchoice == 'paper' and comp_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def display_result(userchoice, comp_choice, result):
    print(f"\nYour choice: {userchoice}")
    print(f"Computer's choice: {comp_choice}")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = userchoice()
        comp_choice = userchoice()

        result = winner(userchoice, comp_choice)
        display_result(userchoice, comp_choice, result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors Game!\n")
    play_game()


