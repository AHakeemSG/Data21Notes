# Hangman game


'''
Things to incorporate:
- user name input,
- functions,
- loops,
- ask the users if they would like to play again
- count of words that have been used
'''

# Import libraries
import random

# List of string data
word_list = ['Word', 'another', 'other', 'something']

name = input("What is your name?  ")
print(f"Hello, {name}! Let's play Hangman!")


# Functions
def retrieve_word():
    word = random.choice(word_list)
    return word.lower()


def play_game(word):
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    num_of_attempts = 10
    print(display_hangman(tries))
    print(word_completion)
    print("\n")


while not guessed and num_of_attempts > 0:
    guess = input("Please guess a letter or a word: ").lower()
    if len(guess) == len(word) and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
        elif guess not in word:
            print(guess, "is not in the word.")
            num_of_attempts -= 1
            guessed_letters.append(guess)
        else:
            print("Good job, ", guess, "is the word")
            guessed_letters.append(guess)
            words_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
            print("You already guessed the word", guess)
        elif guess != word:
            print(guess, "is not the word.")
            num_of_attempts -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
    else:
        print("Not a valid guess. ")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
if guessed:
    print("Congrats, You are the winner!!")
else:
    print("Sorry, you are out of attempts! The word was"+{word}+" , Do you want to try again? ")
    
