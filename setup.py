from setuptools import setup, find_packages

setup(
    name="dice_simulator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dice-simulator=dice_simulator.cli:run_cli',
        ],
    },
    python_requires='>=3.6',
)