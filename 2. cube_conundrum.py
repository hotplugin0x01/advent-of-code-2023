# Date: 04-12-2023
# Author: Wasay

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Part 1
# target = {"red":12, "green":13, "blue":14}

# sum = 0
# for line in lines:
#     valid = True
#     game, cubes = line.split(": ")
#     game_id = int(game.split(" ")[-1])
#     for cube in cubes.split("; "):
#         for colors in cube.split(", "):
#             num, color = colors.split()
#             if int(num) > target[color]:
#                 valid = False
#                 break

#     if valid:
#         sum+= game_id

# print("Part 1: ", sum)


# Part 02
sum = 0
for line in lines:
    game, cubes = line.split(": ")
    game_id = int(game.split(" ")[-1])
    min_set = {"red":1, "green":1, "blue":1}
    for cube in cubes.split("; "):
        for colors in cube.split(", "):
            num, color = colors.split()
            min_set[color] = max(min_set[color], int(num))
    # print(min_set)
    min_set_lst = list(min_set.values())
    prod = min_set_lst[0] * min_set_lst[1] * min_set_lst[2]
    sum += prod

print("Part 2: ", sum)