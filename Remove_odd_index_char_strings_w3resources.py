# Program to remove the characters which have odd index values of a given string (w3 Python String: Exercise-11)
x = 'Nxaxmxexlxexsxs'
y = ''
for i in range(len(x)):
    if i % 2 == 0:
       y += x[i]
print(y)
