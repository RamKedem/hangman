def check_valid_y_n_answer(user_reply):
    while True:
        if user_reply.upper() == 'N':
            return False
        elif user_reply.upper() == 'Y':
            return True
        else:
            print("Please type a valid answer Y or N")
            user_reply = input('Would you like to begin ? (Y/N) : ')


if __name__ == '__main__':
    reply = 'wrong_input'
    print(check_valid_y_n_answer(reply))