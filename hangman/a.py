import sys


tries = 3
word = "slowo"
given_letters = []

user_word = []


def indexes_of_found_letters(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def current_game_state():
    print()
    print(user_word)
    print("Attempts left:", tries)
    print("Letters used:", given_letters)
    print()


for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter: ")
    given_letters.append(letter)

    found_indexes = indexes_of_found_letters(word, letter)

    if len(found_indexes) == 0:
        print("The wrong answer.")
        tries -= 1

        if tries == 0:
            print("End of the game.")
            break
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Way to go! You guessed the word.")
            break

    current_game_state()

