# Date: 01-12-2023
# Author: Wasay

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Part 01
# sum = 0
# for line in lines:
#     num = ''
#     for n in line:
#         if n.isnumeric():
#             num += n
#     if len(num) > 1:
#         n = num[0] + num[-1]
#         sum += int(n)
#     else:
#         n = num + num
#         sum += int(n)

# print("Part 1: ", sum)


# Part 02
digits = {"one":"one1one",
          "two":"two2two",
          "three":"three3three",
          "four":"four4four",
          "five":"five5five",
          "six":"six6six",
          "seven":"seven7seven",
          "eight":"eight8eight",
          "nine":"nine9nine"}

sum = 0
for line in lines:
    for k,v in digits.items():
        line = line.replace(k, v)
    num = ''
    for n in line:
        if n.isnumeric():
            num += n
    if len(num) > 1:
        n = num[0] + num[-1]
        sum += int(n)
    else:
        n = num + num
        sum += int(n)

print("Part 2: ", sum)