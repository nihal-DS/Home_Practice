x = {'a': 1, 'c': 2, 'b': 3}
y = dict(sorted(x.items(), key = lambda x: x[0]))
print(y)