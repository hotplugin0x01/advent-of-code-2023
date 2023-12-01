# Date: 01-12-2023
# Author: Wasay

with open("input.txt") as f:
    data = f.read().strip()

up = 0
down = 0
for i,char in enumerate(data):
    if char == "(":
        up += 1
    else:
        down -= 1

    if (up + down) < 0:
        print(i+1)
        break

# print(up+down)