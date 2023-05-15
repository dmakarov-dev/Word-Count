def count_words(text):
    word_counts = {}
    words = text.lower().split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Prompt the user to enter a text
text = input("Enter some text: ")

# Perform word count analysis
word_counts = count_words(text)

# Print the word count results
print("Word Count Results:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
