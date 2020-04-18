from generate_words import generate_word
from graphics import *

DEBUG = False
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '-'
VALID_YES_REPLIES = ['YES', 'Y']
VALID_NO_REPLIES = ['NO', 'N']


class HangMan(object):
    def __init__(self, word=None):
        self.chosen_word = generate_word() if word is None else word
        self.number_of_guesses = len(HANG_GRAPHICS)
        self.masked_word = PLACEHOLDER * len(self.chosen_word)
        self.used_guesses = set()  # good use of sets, most programmers don't think to use them! :)
        self.wrong_guesses = set()
        self.another_round = True

    @staticmethod
    def begin_user_interaction():
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS) - 1] + '\n')
        print('Welcome to Hangman !\n')
        print("During this game you'll be trying to guess a word.")
        print(
            f"You should try and guess it by suggesting letters within {len(HANG_GRAPHICS)} turns")  # f-strings allow you to add variables in-line easily.
        print("In each turn you're welcome to guess one letter or the entire word\n")

    def display_progress(self):
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS) - self.number_of_guesses] + '\n')
        print(f"[{self.number_of_guesses} guesses left]\nThe word now looks like this : {self.masked_word}")

    def accept_and_examine_user_input(self):
        guess = input("Please type your guess : ")
        while True:
            if guess in self.used_guesses:
                print('You already used this guess')
            elif guess in self.wrong_guesses:
                print('You already tried this guess')
            else:
                return guess
            guess = input("Take another guess : ")

    def check_guess(self, guess):
        if len(guess) == 1:
            return guess in self.chosen_word
        return guess == self.chosen_word

    def correct_guess_operations(self, guess):
        if len(guess) == 1:
            loc = 0
            masked_list = list(self.masked_word)
            for i in range(self.chosen_word.count(guess)):
                masked_list[self.chosen_word.index(guess, loc)] = guess
                loc = self.chosen_word.index(guess, loc) + 1
            self.masked_word = ''.join(masked_list)
            self.used_guesses.add(guess)
        else:
            self.masked_word = guess

    def wrong_guess_operations(self, guess):
        self.number_of_guesses -= 1
        self.wrong_guesses.add(guess)

    @staticmethod
    def init_game():
        while True:
            return HangMan.query_for_yes_no('Ready to begin ? : ')

    @staticmethod
    def query_for_yes_no(question):
        user_input = input(question)
        while True:
            user_input = user_input.upper()
            if user_input in VALID_NO_REPLIES:
                return False
            if user_input in VALID_YES_REPLIES:
                return True

            message = f"Please type a valid input. [{', '.join(VALID_NO_REPLIES)}] for No, [{', '.join(VALID_YES_REPLIES)}] for Yes : "
            user_input = input(message)

    def end_round(self):
        if self.masked_word == self.chosen_word:
            print('Good Job! You guessed the word')
        else:
            print(f"You've failed to guess the word : {self.chosen_word.upper()}")  # converted to an f-string


def game_controller():
    game = HangMan('hello')
    game.begin_user_interaction()
    if not HangMan.init_game():
        return

    while game.number_of_guesses > 0 and game.masked_word != game.chosen_word:
        game.display_progress()
        guess = game.accept_and_examine_user_input()
        if game.check_guess(guess):
            game.correct_guess_operations(guess)
        else:
            game.wrong_guess_operations(guess)
    game.end_round()


if __name__ == "__main__":
    game_controller()
