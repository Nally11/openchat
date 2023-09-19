#need to update forbidden words,

def search_for_curse_words(text):
    curse_words = ["curse1", "curse2", "curse3"]  # Add your curse words here

    # Convert the text to lowercase for case-insensitive matching
    lowercase_text = text.lower()

    # Split the text into individual words
    words = lowercase_text.split()

    # Check if any of the words are curse words
    found_curse_words = []
    for word in words:
        if word in curse_words:
            found_curse_words.append(word)

    return found_curse_words


# Example usage
input_text = input("Enter some text: ")
curse_words_found = search_for_curse_words(input_text)
if curse_words_found:
    print("Curse words found:", curse_words_found)
else:
    print("No curse words found.")
