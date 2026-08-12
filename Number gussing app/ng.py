import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")
    
    while not guessed:
        guess = int(input("Enter your guess: "))
        
        attempts += 1
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            guessed = True
        elif guess < secret_number:
            print(f"Too low! Try again.\n")
        else:
            print(f"Too high! Try again.\n")

def main():
    play_again = True
    
    while play_again:
        number_guessing_game()
        
        response = input("\nDo you want to play again? (yes/no): ").lower()
        if response != 'yes' and response != 'y':
            play_again = False
    
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()