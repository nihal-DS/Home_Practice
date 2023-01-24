# Leet Code 3. Longest Substring Without Repeating Characters
# Description: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
s = "gfdsalkjhg"
window = ''
max_length = 0
for i in s:
    window = window[window.find(i)+1:] + i
    max_length = max(max_length, len(window))
print(max_length)