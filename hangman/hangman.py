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


for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter: ")
    given_letters.append(letter)

    indexes_found = indexes_of_found_letters(word, letter)

    if len(indexes_found) == 0:
        print("The wrong answer.")
        tries -= 1

        if tries == 0:
            print("End of the game.")
            sys.exit(0)

