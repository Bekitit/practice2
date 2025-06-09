def word_counter():
    text = input("Enter a sentence or paragraph:\n")

    words = text.lower().split()

    total_words = len(words)
    print("\nTotal words: " + str(total_words))

    word_freq = {}
    for word in words:
        word = word.strip(".,!?") 
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    print("\nWord Frequencies:")
    for word in word_freq:
        print(word + ": " + str(word_freq[word]))

    most_common = ""
    highest_count = 0
    for word in word_freq:
        if word_freq[word] > highest_count:
            most_common = word
            highest_count = word_freq[word]

    print("\nMost frequent word: '" + most_common + "' (appeared " + str(highest_count) + " times)")
word_counter()
