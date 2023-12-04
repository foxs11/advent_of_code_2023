# f = open('input02.txt', 'r')

# input = f.readlines()

# realCubes = {
#     "red": 12,
#     "green": 13,
#     "blue": 14
# }

# totalNumber = 0

# for i in input :
#     [game, rounds] = i.split(": ")
#     game = game.replace("Game ", "")
#     rounds = rounds.split("; ")
#     newRounds = []
#     for r in rounds:
#         cubes = r.split(", ")
#         colors = {}
#         for c in cubes:
#             [number, color] = c.split(" ")
#             color = color.replace("\n", "")
#             colors[color] = int(number)
#         newRounds.append(colors)
#     flag = True
#     for real in realCubes:
#         for round in newRounds:
#             if real in round:
#                 if realCubes[real] < round[real]:
#                     flag = False
#     if flag:
#         print(game)
#         totalNumber = totalNumber + int(game)

# print(totalNumber)
# f.close



f = open('input02.txt', 'r')

input = f.readlines()

totalNumber = 0

for i in input :
    [game, rounds] = i.split(": ")
    game = game.replace("Game ", "")
    rounds = rounds.split("; ")
    newRounds = []
    for r in rounds:
        cubes = r.split(", ")
        colors = {}
        for c in cubes:
            [number, color] = c.split(" ")
            color = color.replace("\n", "")
            colors[color] = int(number)
        newRounds.append(colors)
    red = 0
    blue = 0
    green = 0
    for new in newRounds:
        if "red" in new:
            if new["red"] > red:
                red = new["red"]
        if "blue" in new:
            if new["blue"] > blue:
                blue = new["blue"]
        if "green" in new:
            if new["green"] > green:
                green = new["green"]
    totalNumber = totalNumber + (red*blue*green)

print(totalNumber)
f.close