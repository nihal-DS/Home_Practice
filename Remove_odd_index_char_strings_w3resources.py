# Program to remove the characters which have odd index values of a given string
x = 'Nxaxmxexlxexsxs'
y = ''
for i in range(len(x)):
    if i % 2 == 0:
       y += x[i]
print(y)