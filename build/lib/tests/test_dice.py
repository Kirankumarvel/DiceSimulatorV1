import pytest
from dice_simulator.dice import roll_dice, InvalidDiceCountError, InvalidSidesError

class TestDiceRolling:
    def test_valid_rolls(self):
        # Test valid dice configurations
        for num_dice in range(1, 7):
            for num_sides in [4, 6, 8, 10, 12, 20]:
                result = roll_dice(num_dice, num_sides)
                assert len(result) == num_dice
                assert all(1 <= x <= num_sides for x in result)

    def test_invalid_dice_count(self):
        with pytest.raises(InvalidDiceCountError):
            roll_dice(0, 6)
        with pytest.raises(InvalidDiceCountError):
            roll_dice(7, 6)

    def test_invalid_sides(self):
        with pytest.raises(InvalidSidesError):
            roll_dice(1, 3)
        with pytest.raises(InvalidSidesError):
            roll_dice(1, 21)