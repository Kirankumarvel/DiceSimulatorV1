from typing import Optional, Tuple
from .dice import roll_dice, InvalidDiceCountError, InvalidSidesError
from .display import display_rolling_animation, display_results

def get_user_input() -> Tuple[int, int]:
    """Get and validate user input for dice rolling"""
    while True:
        try:
            num_dice = int(input("\nHow many dice would you like to roll? (1-6): "))
            num_sides = int(input("How many sides should each die have? (4,6,8,10,12,20): "))
            return num_dice, num_sides
        except ValueError:
            print("Please enter valid numbers.")

def ask_to_continue() -> bool:
    """Ask user if they want to roll again"""
    while True:
        answer = input("\nWould you like to roll again? (y/n): ").lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

def run_cli() -> None:
    """Run the command-line interface"""
    print("Welcome to the Dice Simulator!")
    print("You can roll virtual dice with different numbers of sides.")
    
    while True:
        try:
            num_dice, num_sides = get_user_input()
            
            # Roll with animation
            display_rolling_animation()
            results = roll_dice(num_dice, num_sides)
            
            # Display results
            display_results(results)
            
            # Continue?
            if not ask_to_continue():
                print("\nThanks for using the Dice Simulator. Goodbye!")
                break
                
        except (InvalidDiceCountError, InvalidSidesError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break