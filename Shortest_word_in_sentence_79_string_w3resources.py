# Write a Python program to find the smallest and largest words in a given string
# No. 79 https://www.w3resource.com/python-exercises/string/

string = 'Write a Java program to sort an array of given integers using Quick sort Algorithm'
words = string.split(' ')
lst = []
for i,j in enumerate(words):
    lst.append((i,len(j)))                    # [(index,length),...]
order = sorted(lst,key = lambda a:a[1])       # sorting them based on length
print("Shortest word:", words[order[0][0]])   # words[order[shortest][index]]
print("Longest word:", words[order[-1][0]])   # words[order[longest][index]]