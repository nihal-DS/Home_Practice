# Write a Python program to count characters at the same position
# in a given string (lower and uppercase characters) as in the English
# alphabet.
# No. 78 https://www.w3resource.com/python-exercises/string/

import string
string1 = 'xbcefg'
all_letters = string.ascii_letters
count = 0
for i,j in zip(string1,all_letters):
    if i == j:
        count += 1
print(count)