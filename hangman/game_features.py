

class GameFeaturesMethod:
    def __init__(self, tries, word):
        self.tries = tries
        self.word = word
        self.given_letters = []
        self.user_word = []

    def indexes_of_found_letters(self, letter):
        indexes = []
        for index, letter_in_word in enumerate(self.word):
            if letter == letter_in_word:
                indexes.append(index)
        return indexes

    def current_game_state(self, user_word):
        print()
        print(user_word)
        print("Attempts left:", self.tries)
        print("Letters used:", self.given_letters)
        print()

    def create_hashed_user_word(self):
        for _ in self.word:
            self.user_word.append("_")

