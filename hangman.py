from generate_words import generate_word
from graphics import *
from string import ascii_lowercase
from helpers import *


ASCII = list(ascii_lowercase)
DEBUG = False
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '-'


class HangMan(object):
    def __init__(self, word=None):
        self.chosen_word = generate_word() if word is None else word
        self.number_of_guesses = len(HANG_GRAPHICS)
        self.masked_word = PLACEHOLDER * len(self.chosen_word)
        self.g_letter = ''
        self.used_letters = set()
        self.wrong_letters = set()
        self.another_round = True

    @staticmethod
    def begin_user_interaction():
        clear()
        print('Welcome to Hangman !')

    @staticmethod
    def ask_begin_game():
        user_input = input('Would you like to begin ? (Y/N) : ')
        return check_valid_y_n_answer(user_input)

    def check_valid_guess(self,user_input):
        user_input = user_input.lower()
        while True:
            if len(user_input) == 1:
                if user_input in self.used_letters:
                    print('You already used that letter')
                    continue
                elif user_input in self.wrong_letters:
                    print('You already tried this letter')
                    continue
                elif user_input not in ASCII:
                    print('Not a valid letter')
                    continue
                else:
                    return user_input
            else:
                print('Your guess should have only one letter')
                continue
            user_input = input("Please try again : ")

    def guess_letter(self):
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS) - self.number_of_guesses])
        print("[{} guesses left]\nThe word now looks like this : {}"
              .format(self.number_of_guesses, self.masked_word))
        user_input = input("Guess a letter : ")
        self.g_letter = self.check_valid_guess(user_input)

    def correct_guess(self):
        loc = 0
        masked_list = list(self.masked_word)
        for i in range(self.chosen_word.count(self.g_letter)):
            masked_list[self.chosen_word.index(self.g_letter, loc)] = self.g_letter
            loc = self.chosen_word.index(self.g_letter, loc) + 1
        self.masked_word = ''.join(masked_list)
        self.used_letters.add(self.g_letter)

    def wrong_guess(self):
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS) - self.number_of_guesses])
        self.number_of_guesses -= 1
        self.wrong_letters.add(self.g_letter)

    def check_guess(self):
        if self.g_letter in self.chosen_word:
            return True
        else:
            return False

    def end_round(self):
        if self.masked_word == self.chosen_word:
            print('Good Job! You\'ve guessed the word')
        else:
            print('You\'ve faild to guess the word : {}'
                  .format(self.chosen_word.upper()))

    def play(self):
        self.begin_user_interaction()
        if self.ask_begin_game():
            while self.chosen_word != self.masked_word \
                    and self.number_of_guesses > 0:
                self.guess_letter()
                if self.check_guess():
                    self.correct_guess()
                else:
                    self.wrong_guess()
            self.end_round()


def game_controller():
    game = HangMan()
    game.play()


if __name__ == "__main__":
    game_controller()
