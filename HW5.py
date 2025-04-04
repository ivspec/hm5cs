
# File: HW5.py
# Author: Isaac Villanueva, Nicholas Hinkel
# UT EID: imv367, nsh748
# Course: CS 303E
#
# This program picks a random word, takes user's input of a letter, and prints 
# dashes of the amount of letters of the random word, replacing the dash with
# users input when correct, and repeats until user has run out of guesses or
# guessed correctly.

import random

def load_words(filename):
    """
    Creates a list of words from the file contents

    Parameters
    ----------
    filename : str
        Name of the file to be processed, contains a single word on each line
    
    Returns
    -------
    word_list : list or str
        List of words, each element is a word from the file
    """
    word_list = []
    try:
        file = open(filename, "r")
        for line in file:
            word = line.strip()
            word_list.append(word)
        file.close()
    except FileNotFoundError:
        print("File not found. Please ensure that 'words.txt' is in the same \
              folder.")
    return word_list

def play_hangman():
    """
    Runs a Hangman game where user input guesses letters to a selected random
    word. The game prints the amount of dashes that the word is, and each dash 
    corresponds to an unguessed letter. If the user guesses correctly,
    the dash is replaced with the correct letter.
    If the user is incorrect, the amount of remaining guesses decreases.
    The function keeps accepting input until the guess is correct or user runs
    out of guesses.

    Parameters
    ----------
    
    Returns
    -------

    """
    # words = load_words("words.txt") 
    # word = random.choice(words) 
    
    word = "banjo"

    dashes = "-" * len(word)
    print("Let's play hangman!")
    print(dashes)

    guessed_letters = [] 
    remaining_guesses = 8 

    while remaining_guesses > 0 and dashes != word:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("That is not a letter. Enter a letter.")
        else:
            already_guessed = False
            for letter in guessed_letters:
                if guess == letter:
                    already_guessed = True

            if already_guessed:
                print(f"You've already guessed {guess}")
            else:
                guessed_letters.append(guess)

                found = False
                for letter in word:
                    if letter == guess:
                        found = True

                if not found:
                    remaining_guesses -= 1

                new_dashes = ""

                # Itterates through each letter of the word until the players
                # input matches a letter in the word and replaces teh "-" with
                # the letter. Otherwise continue using "-"
                for i in range(len(word)):
                    letter_found = False
                    for guessed in guessed_letters:
                        if word[i] == guessed:
                            letter_found = True
                    if letter_found:
                        new_dashes += word[i]
                    else:
                        new_dashes += "-"

                dashes = new_dashes
                print(dashes)

                if (dashes != word):
                    print(f"You have {remaining_guesses} tries remaining.")

    if dashes == word:
        print("You win!")
    else:
        print(f"You lose. The word was {word}.")


def main():
    play_hangman()

if __name__ == '__main__':
    main()
