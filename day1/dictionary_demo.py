def calculate_word_frequency(text):
    # Removing punctuation and converting to lowercase
    text = text.lower()
    for char in "-.,\n":
        text = text.replace(char, " ")

    # Splitting the text into words
    words = text.split()

    # Creating a dictionary to hold the frequency of each word
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


def main():
    # Sample text about turtles
    text = """
    Turtles are amazing creatures. They have been around for over 200 million years. Turtles can be found in almost every type of climate, from deserts to rainforests. Some turtles are very small, while others can grow quite large. Turtles have a hard shell that protects them from predators. Interestingly, turtles also play a vital role in their ecosystems. By eating various plants and animals, turtles help to maintain a balanced environment.
    """

    # Calculating word frequency
    word_freq = calculate_word_frequency(text)

    # Printing the word frequency
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
