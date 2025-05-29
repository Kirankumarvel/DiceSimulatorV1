# 🎲 Dice Simulator 

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A customizable dice rolling simulator package with command-line interface and visual feedback.

## Features

- 🎲 Roll 1-6 dice at a time
- ⚡ Choose from standard dice sizes (4, 6, 8, 10, 12, 20 sides)
- 🌟 Visual rolling animation
- 🖥️ ASCII art dice faces for single rolls
- ✅ Comprehensive error handling
- 🧪 Unit tested with pytest

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Recommended Installation (Development Mode)
```bash
git clone https://github.com/Kirankumarvel/DiceSimulatorV1.git
cd DiceSimulatorV1
pip install -e .
```

### Alternative Installations
```bash
# User installation (no admin required)
pip install --user -e .

# System-wide installation (requires admin)
pip install .
```

## Usage

### Command Line Interface
```bash
dice-simulator
```

### Programmatic Usage
```python
from dice_simulator import roll_dice

# Roll 3 eight-sided dice
results = roll_dice(num_dice=3, num_sides=8)
print(f"Results: {results}")
print(f"Total: {sum(results)}")
```

## Project Structure
```
dice_simulator/
├── dice_simulator/
│   ├── __init__.py
│   ├── dice.py           # Core dice rolling logic
│   ├── display.py        # Visual components
│   ├── cli.py            # Command-line interface
│   └── exceptions.py     # Custom exceptions
├── tests/
│   ├── test_dice.py
│   ├── test_display.py
│   └── test_cli.py
├── setup.py
└── README.md
```

## Development

### Running Tests
```bash
pytest tests/
```

### Building for Distribution
```bash
python -m build
```

### Creating Requirements File
```bash
pip freeze > requirements.txt
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ASCII dice art inspired by various open-source projects
- Python packaging best practices from PyPA

---

Enjoy rolling! 🎲✨
