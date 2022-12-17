x = int(input("Enter the value of x: "))
n = int(input("Enter the length of the sequence: "))
final = 0
for i in range(1, n+1):
    if i % 2 != 0:
        final = final - (x ** i)
    else:
        final = final + (x ** i)
print(final)
