# Program to count the occurrences of each word in a given sentence
x = '''Too many nights I went famous
    Too many nights I went nameless
    Too many nights I went brainless'''
words = dict()
word_list = x.split()

for i in word_list:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

print(words)