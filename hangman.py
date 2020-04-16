from generate_words import generate_word
from graphics import *

DEBUG = False
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '-'
VALID_YES_REPLIES = ['YES','Y']
VALID_NO_REPLIES = ['NO','N']


class HangMan(object):
    def __init__(self, word=None):
        self.chosen_word = generate_word() if word is None else word
        self.number_of_guesses = len(HANG_GRAPHICS)
        self.masked_word = PLACEHOLDER * len(self.chosen_word)
        self.g_string = ''
        self.used_guesses = set()
        self.wrong_guesses = set()
        self.another_round = True

    @staticmethod
    def begin_user_interaction():
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS)-1] + '\n')
        print('Welcome to Hangman !\n')
        print('During this game you\'ll be trying to guess a word.')
        print('You should try and guess it by suggesting letters within {} turns'\
              .format(len(HANG_GRAPHICS)))
        print('In each turn you\'re welcome to guess one letter or the entire word\n')

    @staticmethod
    def check_valid_y_n_answer(user_reply):
        user_reply = user_reply.upper()
        if user_reply in VALID_NO_REPLIES:
            return False
        elif user_reply in VALID_YES_REPLIES:
            return True

    @staticmethod
    def ask_begin_game():
        user_input = input('Ready to begin ? : ')
        return user_input

    def check_guess_already_used(self, user_input):
        if user_input in self.used_guesses:
            return True
        else:
            return False

    def check_wrong_guess_already_tried(self, user_input):
        if user_input in self.wrong_guesses:
            return True
        else:
            return False

    @staticmethod
    def check_only_one_letter(user_input):
        if len(user_input) == 1:
            return True
        else:
            return False

    def display_progress(self):
        clear()
        print(HANG_GRAPHICS[len(HANG_GRAPHICS) - self.number_of_guesses] + '\n')
        print("[{} guesses left]\nThe word now looks like this : {}"
              .format(self.number_of_guesses, self.masked_word))

    def accept_and_examine_user_input(self):
        guess = input("Please type your guess : ")
        while True:
            if self.check_guess_already_used(guess):
                print('You already used this guess')
            elif self.check_wrong_guess_already_tried(guess):
                print('You already tried this guess')
            else:
                return guess
            guess = input("Take another guess : ")

    def check_guess(self):
        if self.check_only_one_letter(self.g_string):
            if self.g_string in self.chosen_word:
                return True
            else:
                return False
        else:
            if self.g_string == self.chosen_word:
                return True
            else:
                return False

    def correct_guess_operations(self):
        if self.check_only_one_letter(self.g_string):
            loc = 0
            masked_list = list(self.masked_word)
            for i in range(self.chosen_word.count(self.g_string)):
                masked_list[self.chosen_word.index(self.g_string, loc)] = self.g_string
                loc = self.chosen_word.index(self.g_string, loc) + 1
            self.masked_word = ''.join(masked_list)
            self.used_guesses.add(self.g_string)
        else:
            self.masked_word = self.g_string

    def wrong_guess_operations(self):
        self.number_of_guesses -= 1
        self.wrong_guesses.add(self.g_string)

    def init_game(self):
        user_initial_reply = self.ask_begin_game()
        while True:
            if self.check_valid_y_n_answer(user_initial_reply) is None:
                message = 'Please type a valid input. [{}] for No, [{}] for Yes : '
                user_initial_reply = input(message.format(', '.join(VALID_NO_REPLIES),
                                                          ', '.join(VALID_YES_REPLIES)))
            elif self.check_valid_y_n_answer(user_initial_reply):
                return True
            else:
                return False

    def end_round(self):
        if self.masked_word == self.chosen_word:
            print('Good Job! You guessed the word')
        else:
            print('You\'ve failed to guess the word : {}'
                  .format(self.chosen_word.upper()))


def game_controller():
    game = HangMan('hello')
    game.begin_user_interaction()
    if game.init_game():
        while game.number_of_guesses > 0 and game.masked_word != game.chosen_word:
            game.display_progress()
            game.g_string = game.accept_and_examine_user_input()
            if game.check_guess():
                game.correct_guess_operations()
            else:
                game.wrong_guess_operations()
        game.end_round()


if __name__ == "__main__":
    game_controller()
