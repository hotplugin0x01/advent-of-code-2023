# Date: 01-12-2023
# Author: Wasay

with open("input.txt") as f:
    data = f.read().strip()

up = 0
down = 0
for char in data:
    if char == "(":
        up += 1
    else:
        down -= 1

print(up+down)