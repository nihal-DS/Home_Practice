# Write a Python program that accepts a comma separated sequence of words as input and
# prints the unique words in sorted form (alphanumerically).
x = input("Enter values: ")
y = x.split(",")
print(",".join(sorted(list(set(y)))))