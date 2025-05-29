import time
from typing import List

def display_rolling_animation(duration: float = 1.5) -> None:
    """Show a simple rolling animation"""
    symbols = ["/", "-", "\\", "|"]
    end_time = time.time() + duration
    
    try:
        while time.time() < end_time:
            for symbol in symbols:
                print(f"\rRolling... {symbol}", end="", flush=True)
                time.sleep(0.1)
        print("\r" + " " * 15 + "\r", end="")  # Clear the animation line
    except (KeyboardInterrupt, Exception) as e:
        print("\nAnimation interrupted")

def display_results(rolls: List[int]) -> None:
    """Display the dice roll results"""
    if not rolls:
        print("No results to display")
        return
    
    print(f"\nResults: {', '.join(map(str, rolls))}")
    print(f"Total: {sum(rolls)}")
    
    # Show a simple dice face for single die rolls
    if len(rolls) == 1:
        print("\n" + get_dice_face(rolls[0]))

def get_dice_face(value: int) -> str:
    """Return ASCII art for a dice face"""
    faces = {
        1: ("┌─────────┐\n"
            "│         │\n"
            "│    ●    │\n"
            "│         │\n"
            "└─────────┘"),
        2: ("┌─────────┐\n"
            "│ ●       │\n"
            "│         │\n"
            "│       ● │\n"
            "└─────────┘"),
        3: ("┌─────────┐\n"
            "│ ●       │\n"
            "│    ●    │\n"
            "│       ● │\n"
            "└─────────┘"),
        # Add more faces as needed
    }
    return faces.get(value, f"[ {value} ]")  # Default simple display