import random

def roll_dice(num_dice, sides):
    """Roll dice and return the results"""
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def main():
    print("=== Dice Roller ===")
    
    # Get number of dice
    num_dice = int(input("How many dice do you want to roll? "))
    
    # Get number of sides
    sides = int(input("How many sides on each die? (e.g., 6 for d6) "))
    
    # Roll the dice
    results = roll_dice(num_dice, sides)
    
    # Show results
    print("\nDice rolls:", results)
    print("Total:", sum(results))

# Run the program
if __name__ == "__main__":
    main()
