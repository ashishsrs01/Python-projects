import time
import sys


def countdown_timer():
    print("\n" + "="*50)
    print("\033[1;36m" + "COUNTDOWN TIMER".center(50) + "\033[0m")
    print("="*50 + "\n")

    while True:
        try:
            seconds = int(input("\033[1;33mEnter seconds for the timer: \033[0m"))
            if seconds <= 0:
                print("\033[91mPlease enter a positive number greater than 0!\033[0m\n")
                continue
            break
        except ValueError:
            print("\033[91mPlease enter a valid number!\033[0m\n")

    print("\n\033[92mTimer started!\033[0m\n")
    
    remaining_seconds = seconds
    
    while remaining_seconds > 0:
        mins = remaining_seconds // 60
        secs = remaining_seconds % 60
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # Clear line and display timer
        sys.stdout.write(f"\r\033[1;36m{timer_display}\033[0m")
        sys.stdout.flush()
        
        time.sleep(1)
        remaining_seconds -= 1
    
    print("\r\033[1;32m00:00 ✓ Time's up! ⏰\033[0m\n")
    print("\033[1;33m🔔 Beep! Beep! Beep! 🔔\033[0m\n")
    
    while True:
        again = input("\033[1;33mDo you want to set another timer? (yes/no): \033[0m").strip().lower()
        if again in ['yes', 'y']:
            print()
            countdown_timer()
            break
        elif again in ['no', 'n']:
            print("\n" + "="*50)
            print("\033[1;32m" + "Thanks for using the timer! Goodbye!".center(50) + "\033[0m")
            print("="*50 + "\n")
            break
        else:
            print("\033[91mPlease enter 'yes' or 'no'.\033[0m\n")


if __name__ == "__main__":
    countdown_timer()
