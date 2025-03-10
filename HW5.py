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
    words = random.choice(load_words("words.txt"))
    print(words)
    print("Let's play hangman!")
    print("-" * len(words))

    guess = input(str("Guess a letter: "))

    while str.isalpha(guess) == False:
        print("That is not a letter. Enter a letter.")
        guess = input(str("Guess a letter: "))
    

def main():
    play_hangman()

if __name__ == '__main__':
    main()