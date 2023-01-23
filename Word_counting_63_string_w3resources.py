# Write a Python program to generate two strings from a given string.
# For the first string, use the words that occur only once, and
# for the second, use the words that occur multiple times in the
# said string.
# No. 68 https://www.w3resource.com/python-exercises/string/

from collections import Counter
string1 = 'here we go again but where are we even going is it here'
words = list(string1.split(' '))
count = Counter(words)
repeated = ''
not_repeated = ''
for key,value in count.items():
    if value > 1:
        repeated = repeated + key + ' '
    else:
        not_repeated = not_repeated + key + ' '
print(repeated)
print(not_repeated)