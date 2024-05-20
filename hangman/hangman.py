import sys
from game_features import GameFeaturesMethod


class RunGame(GameFeaturesMethod):
    def __init__(self, tries, word):
        super().__init__(tries, word)

    def run(self):
        self.create_hashed_user_word()
        while True:
            letter = input("Enter a letter: ")
            self.given_letters.append(letter)

            found_indexes = self.indexes_of_found_letters(letter)

            if len(found_indexes) == 0:
                print("The wrong answer.")
                self.tries -= 1

                if self.tries == 0:
                    print("End of the game.")
                    sys.exit(0)
            else:
                for index in found_indexes:
                    self.user_word[index] = letter

                if "".join(self.user_word) == self.word:
                    print("Way to go! You guessed the word.")
                    sys.exit(0)

            self.current_game_state(self.user_word)


if __name__ == "__main__":
    name = input("Hi! Welcome in my game Hangman. What is your name?: ").capitalize()
    word = input(f"{name} to start game please set your word!: ")
    tries = int(input(f"{name} You can define how many tries you need?: "))
    print("Let's play!")
    a = RunGame(tries=tries, word=word)
    a.run()

