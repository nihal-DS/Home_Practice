nums = []
y = []
a = 0
for i in range(len(nums) - 1):
    if nums[i+1] != nums[i] + 1:
        if a == i:
            y.append(f"{nums[i]}")
        else:
            y.append(f"{nums[a]}->{nums[i]}")
        a = i + 1
if a == len(nums) - 1:
    y.append(f"{nums[-1]}")
else:
    y.append(f"{nums[a]}->{nums[-1]}")
print(y)