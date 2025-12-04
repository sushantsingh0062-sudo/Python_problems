# Word frequency counter from a paragraph (use dict).
paragraph = "This is a sample paragraph. This paragraph is for testing word frequency counter."
words = paragraph.lower().replace('.', '').split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequency Counter:", word_freq)