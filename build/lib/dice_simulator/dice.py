import random
from typing import List

class DiceError(Exception):
    """Base exception for dice-related errors"""
    pass

class InvalidDiceCountError(DiceError):
    """Raised when an invalid number of dice is requested"""
    pass

class InvalidSidesError(DiceError):
    """Raised when an invalid number of sides is requested"""
    pass

def validate_input(num_dice: int, num_sides: int) -> None:
    """Validate dice input parameters"""
    if not 1 <= num_dice <= 6:
        raise InvalidDiceCountError("Number of dice must be between 1 and 6")
    
    valid_sides = {4, 6, 8, 10, 12, 20}
    if num_sides not in valid_sides:
        raise InvalidSidesError("Number of sides must be one of: 4, 6, 8, 10, 12, 20")

def roll_dice(num_dice: int, num_sides: int) -> List[int]:
    """
    Simulate rolling dice and return the results
    
    Args:
        num_dice: Number of dice to roll (1-6)
        num_sides: Number of sides per die (4,6,8,10,12,20)
    
    Returns:
        List of dice roll results
    
    Raises:
        InvalidDiceCountError: If num_dice is invalid
        InvalidSidesError: If num_sides is invalid
    """
    validate_input(num_dice, num_sides)
    return [random.randint(1, num_sides) for _ in range(num_dice)]