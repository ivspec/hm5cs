
# File: HW5.py
# Author: Isaac Villanueva, Nicholas Hinkel
# UT EID: imv367, nsh748
# Course: CS 303E
#
# .

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
