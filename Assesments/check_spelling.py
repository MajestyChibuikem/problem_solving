from textblob import TextBlob #type: ignore
word = input("Enter your word: ")
blob = TextBlob(word)

if blob.correct() == word:
    print("Correct word")
else:
    correct_word = blob.correct()
    print(f"Correct spelling: {correct_word}")


