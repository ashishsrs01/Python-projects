import random

# Global score values
score_user = 0
score_computer = 0


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    global score_user, score_computer

    print("\n" + "="*50)
    print("\033[1;36m" + "ROCK PAPER SCISSORS GAME".center(50) + "\033[0m")
    print("="*50 + "\n")

    while True:
        print("\033[1;33mChoose your move:\033[0m")
        print("  \033[92m1.\033[0m Rock")
        print("  \033[92m2.\033[0m Paper")
        print("  \033[92m3.\033[0m Scissors")
        print("  \033[92m4.\033[0m View Score")
        print("  \033[92m5.\033[0m Reset Score")
        print("  \033[91m6.\033[0m Quit")
        print()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            user_choice = "rock"
        elif choice == "2":
            user_choice = "paper"
        elif choice == "3":
            user_choice = "scissors"
        elif choice == "4":
            print(f"\n\033[1;36mCurrent Score:\033[0m")
            print(f"  You: \033[92m{score_user}\033[0m")
            print(f"  Computer: \033[92m{score_computer}\033[0m\n")
            continue
        elif choice == "5":
            score_user = 0
            score_computer = 0
            print("\n\033[93mScore has been reset!\033[0m\n")
            continue
        elif choice == "6":
            print("\n" + "="*50)
            print("\033[1;32m" + "Thanks for playing! Goodbye!".center(50) + "\033[0m")
            print("="*50 + "\n")
            break
        else:
            print("\033[91mInvalid choice. Please select 1-6.\033[0m\n")
            continue

        computer_choice = get_computer_choice()
        result = get_winner(user_choice, computer_choice)

        if result == "You win!":
            score_user += 1
        elif result == "Computer wins!":
            score_computer += 1

        print(f"\n\033[1;36mYou chose:\033[0m \033[92m{user_choice.upper()}\033[0m")
        print(f"\033[1;36mComputer chose:\033[0m \033[92m{computer_choice.upper()}\033[0m")
        print(f"\033[1;33m{result}\033[0m")
        print(f"Score - You: \033[92m{score_user}\033[0m  Computer: \033[92m{score_computer}\033[0m\n")


if __name__ == "__main__":
    play_game()

