x = -121
if x < 0:
    print(False)
y = ''
for i in reversed(str(x)):
    print(i)
    y += i
if int(y) - x == 0:
    print(True)