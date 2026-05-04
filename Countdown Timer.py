import time

def countdown_timer(seconds):
    """A simple countdown timer that counts down from the given seconds."""
    
    print(f"Timer started! Counting down from {seconds} seconds...\n")
    
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        
        # Format the display with leading zeros
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"Time remaining: {timer_display}", end="\r")
        
        time.sleep(1)
        seconds -= 1
    
    # Timer finished
    print("\nTime's up! ⏰")
    print("Beep! Beep! Beep!")

def main():
    """Main function to run the countdown timer."""
    
    print("=" * 40)
    print("Welcome to the Countdown Timer!")
    print("=" * 40)
    
    try:
        # Get input from user
        user_input = input("\nEnter the number of seconds: ")
        seconds = int(user_input)
        
        # Validate input
        if seconds < 0:
            print("Please enter a positive number!")
            return
        
        if seconds == 0:
            print("Timer must be greater than 0!")
            return
        
        # Run the countdown timer
        countdown_timer(seconds)
        
    except ValueError:
        print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    main()
