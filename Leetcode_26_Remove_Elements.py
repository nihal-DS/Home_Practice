# Leetcode No.26 Remove Elements https://leetcode.com/problems/remove-element/

x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
p1 = 0
p2 = 0
while p2 < len(x):
    if x[p1] == x[p2]:
        p2 += 1
    else:
        x[p1 + 1] = x[p2]
        p1 += 1
        p2 += 1

print(x)
print(p1 + 1)