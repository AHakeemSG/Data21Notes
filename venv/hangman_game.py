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

# Variables
guessed = False
guessed_letters = []
guessed_words = []
num_of_attempts = 10
completed_word = ''
# print(display_hangman(tries))
# print(word_completion)
print("\n")


# Functions
def retrieve_word():
    return random.choice(word_list).lower()


def play_game(word):
    global guessed, num_of_attempts

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
                words_as_list = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                completed_word = "".join(word_as_list)
                if "_" not in completed_word:
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
                completed_word = word
        else:
            print("Not a valid guess. ")
       # print(display_hangman(num_of_attempts))
        print(completed_word)
        print("\n")
    if guessed:
        print("Congrats, You are the winner!!")
    else:
        print(f"Sorry, you are out of attempts! The word was {word} , Do you want to try again? ")


def main_game():
    word = retrieve_word()
    completed_word = "_" * len(word)
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get.word()
        play(word)


if _name_ == "_main_":
    main()
