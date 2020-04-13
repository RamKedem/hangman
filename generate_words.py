import random

SOURCE= 'data.txt'


def generate_word(source = SOURCE):
    with open(source, 'r') as f:
        available_words = f.readlines()
    chosen_word = random.choice(available_words)
    return chosen_word.strip('\n')


if __name__ == '__main__':
    print(generate_word())