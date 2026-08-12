import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")
    
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                guessed = True
            elif guess < secret_number:
                print(f"Too low! Try again.\n")
            else:
                print(f"Too high! Try again.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

def main():
    play_again = True
    
    while play_again:
        try:
            number_guessing_game()
        except Exception as e:
            print(f"An error occurred: {e}")
        
        while True:
            try:
                response = input("\nDo you want to play again? (yes/no): ").lower().strip()
                if response in ['yes', 'y']:
                    break
                elif response in ['no', 'n']:
                    play_again = False
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            except Exception as e:
                print(f"Error reading input: {e}")
    
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()