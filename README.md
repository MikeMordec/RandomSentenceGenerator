# RandomSentenceGenerator

A Python application that generates random sentences from a predefined word grid and performs entropy analysis on the selected words. This project showcases creative writing through randomness, providing a unique way to explore word combinations and their informational content.

## Features

- **Random Sentence Generation**: Constructs sentences using randomly selected words from a grid.
- **Entropy Analysis**: Calculates and displays entropy values based on user input to assess the randomness of word selections.
- **Customizable Word Grid**: Easily modify the word grid to include any words or phrases for personalized sentence generation.

## How It Works

1. The program initializes a grid of words from predefined lists and an optional CSV file.
2. It randomly selects a specified number of words to generate sentences.
3. Users can input entropy values related to the word grids, and the program calculates the total entropy.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RandomSentenceGenerator.git

    Navigate to the project directory:

    bash

    cd RandomSentenceGenerator

    Ensure you have Python installed on your system.

Usage

    Update the words.csv file with your desired words, if applicable.

    Run the main script:

    bash

    python main.py

    Follow the prompts to generate sentences and provide entropy analysis.

Code Structure

    main.py: The main script that executes the program.
    words.csv: A CSV file containing additional words for the word grid (optional).
