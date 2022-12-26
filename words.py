def print_upper_words (words, must_start_with):
    """Prints a list of words in upper case if thier first letter starts with one of the letters specified"""

    for word in words:
        word = word.upper()
        for letter in must_start_with:
            letter = letter.upper()
            if (word.startswith(letter)):
                print (f"{word}")

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})