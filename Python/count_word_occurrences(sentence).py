def count_word_occurrences(sentence):
    word_list = sentence.split()
    unique_words = []
    word_counts = []

    for word in word_list:
        if word in unique_words:
            index = unique_words.index(word)
            word_counts[index] += 1
        else:
            unique_words.append(word)
            word_counts.append(1)

    return unique_words, word_counts

# User input
user_sentence = input("Enter a sentence: ")

unique_words, word_counts = count_word_occurrences(user_sentence)
print("Word occurrences in the sentence:")
for word, count in zip(unique_words, word_counts):
    print("{word}: {count}")