
# 📘 Assignment: Hangman Game

## 🎯 Objective

Practice Python control flow, string manipulation, and user interaction by building a Hangman-style word guessing game.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a Hangman game that selects a secret word from a predefined list and lets the player guess letters until they win or lose.

#### Requirements
Completed program should:

- Randomly choose a secret word from a list of at least 5 words.
- Display the current word progress with underscores for hidden letters, for example: `_ a _ _ m a n`.
- Accept single-letter guesses from the player and update the displayed progress.
- Track and display the number of incorrect guesses remaining.
- End the game when the player guesses the word or uses all allowed attempts.
- Show a win message if the word is guessed, or a lose message with the correct word if attempts run out.

### 🛠️ Add Guess Validation and Replay Option

#### Description
Improve the game by validating input and giving the player the option to play again.

#### Requirements
Completed program should:

- Reject invalid input such as numbers, multiple characters, or empty guesses.
- Prevent the player from guessing the same letter more than once.
- Prompt the player to play again after the game ends.
- Reset the game state correctly when starting a new round.
