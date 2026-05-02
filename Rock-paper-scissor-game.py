import random 

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "it's a tie!"
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    else:
        return "Computer wins!"

def play_game():

    score = {'user': 0, 'computer': 0}
    
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'scores' to view current scores, or 'quit' to exit the game.")

    while True:
        user_choice = input().lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            if score['user'] > score['computer']:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - You won! 🎉")
            elif score['user'] < score['computer']:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - Computer won! 😞")
            else:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - It's a tie! 🤝")
            break

        elif user_choice == "scores":
            if score['user'] > score['computer']:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - You are leading! 👏")
            elif score['user'] < score['computer']:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - Computer is leading! 👎")
            else:
                print(f"Current Score - You: {score['user']} | Computer: {score['computer']} - It's a tie going strong! 🤝")
        
        else:
            print("it's invalid choice. Please choose rock, paper, scissors, 'scores' or 'quit'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = get_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            score['user'] += 1
        elif result == "Computer wins!":
            score['computer'] += 1

    

