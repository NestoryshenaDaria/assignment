import re
from collections import Counter


def word_frequency(text):
    words = re.findall(r'\w+', text.lower())

    word_counts = Counter(words)

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_words


text = input("Enter the text: ")

result = word_frequency(text)

for word, count in result:
    print(f"{word}: {count}")

total_words = len(result)
unique_words = len(set(word for word, count in result))
most_common_word, most_common_count = result[0]

print("Additional Statistics:")
print(f"Total words: {total_words}")
print(f"Unique words: {unique_words}")
print(f"Most common word: {most_common_word} (Count: {most_common_count})")
