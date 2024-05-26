import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def int_check(user_input):
    while True:
        if user_input.isdigit():
            user_input = float(user_input)
            return user_input
            break
        else:
            print("Incorrect format, Please try again: ")
            user_input = input("Try again: ")
    pass