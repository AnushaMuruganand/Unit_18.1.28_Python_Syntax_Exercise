def print_upper_words(list):
    """Print each word on sep line, uppercased."""

    for word in list:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

print("\n\n")

def print_upper_words2(list , must_start_with):
    """Print each word on sep line, uppercased, if starts with ONLY one of the given letter passed in."""

    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})