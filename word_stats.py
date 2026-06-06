def word_count(text):
    return len(text.split())


def char_count(text):
    return len(text.replace(" ", ""))


def longest_word(text):
    words = text.split()
    return max(words, key=len)


sentence = input("Enter a sentence: ")

print("Word count:", word_count(sentence))
print("Character count:", char_count(sentence))
print("Longest word:", longest_word(sentence))