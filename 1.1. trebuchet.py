# Date: 01-12-2023
# Author: Wasay

with open("input.txt") as f:
    lines = f.read().split("\n")

nums = []
sum = 0
for line in lines:
    num = ''
    for n in line:
        if n.isnumeric():
            num += n
    if len(num) > 1:
        n = num[0] + num[-1]
        sum += int(n)
        nums.append(int(n))
    else:
        n = num + num
        nums.append(int(n))
        sum += int(n)


# print(len(nums))
print(sum)

