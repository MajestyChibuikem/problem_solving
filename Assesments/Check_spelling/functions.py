import re

# Load a dictionary of correctly spelled words
def load_dictionary(file_path):
    with open(file_path, "r") as f:
        return set(word.strip().lower() for word in f)

# Check if a word is misspelled
def is_misspelled(word, dictionary):
    return word.lower() not in dictionary

# Check spellings in a given text
def check_spellings(text, dictionary):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Find misspelled words
    misspelled = [word for word in words if is_misspelled(word, dictionary)]

    return misspelled

#checks if the input is a string and loops back if not
def str_check(user_input):
    while True:
        if user_input.isdigit():
            user_input = input("Wrong input format, try again: ")
        else:
            return (user_input)
