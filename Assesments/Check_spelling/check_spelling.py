import functions

text = "Ths is an example of a sentense wth some mispelled words."

text = input("Input your text: ")
text = functions.str_check(text)
# Load dictionary
dictionary = functions.load_dictionary("Assesments/Check_spelling/dictionary.txt")

# Check spellings
misspelled_words = functions.check_spellings(text, dictionary)

if misspelled_words:  # Check if misspelled_words list is not empty
    print("Misspelled words found:")
    for word in misspelled_words:
        print(word)
else:
    print("No misspelled words found.")
