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
        print("File not found. Please ensure that 'words.txt' is in the same folder.")
    return word_list

def play_hangman():
    load_words("words.txt")
    word = random.choice(load_words("words.txt"))
    print(word)
    print("Let's play hangman!")
    dashes = "-" * len(word)
    print(dashes)
    print(dashes[1])

    guessed_letters = []
 

    guess = input(str("Guess a letter: "))
    guess = str.lower(guess)

    while str.isalpha(guess) == False:
        print("That is not a letter. Enter a letter.")
        guess = input(str("Guess a letter: "))
        guess = str.lower(guess)

    guessed_letters.append(guess)

    if guess in guessed_letters:
            print(f"You've already guessed {guess}")


def main():
    play_hangman()

if __name__ == '__main__':
    main()
