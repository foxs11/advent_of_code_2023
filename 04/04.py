# f = open('04/input04.txt', 'r')
# input = f.readlines()

# total = 0

# for i in input:
#     winning = 0
#     game = i.split(": ")
#     game[1] = game[1].replace("\n", "").replace("  ", " ").lstrip()
#     numbers = game[1].split(" | ")
#     winningNumbers = numbers[0].split(" ")
#     myNumbers = numbers[1].split(" ")
#     for n in winningNumbers:
#         if n in myNumbers:
#             if winning == 0:
#                 winning = 1
#             else:
#                 winning = winning * 2
#     total = total + winning

# print(total)

# f.close()


f = open('04/input04.txt', 'r')
input = f.readlines()

total = 0

newCards = []

cardlist = {}

for i in input:
    game = i.split(":")
    game[1] = game[1].replace("\n", "").replace("  ", " ").lstrip()
    game[0] = game[0].replace("Card", "").lstrip()
    newCards.append(game)
    cardlist[game[0]] = game[1]


# print(newCards)
# print(cardlist)

for card in newCards:
    # print(len(newCards))
    winning = 0
    numbers = card[1].split(" | ")
    winningNumbers = numbers[0].split(" ")
    myNumbers = numbers[1].split(" ")
    for n in winningNumbers:
        if n in myNumbers:
            winning = winning + 1
    # print(winning)
    for x in range(winning):
        num = str(int(card[0]) + x + 1)
        # print(num)
        newCards.append([num, cardlist[num]])

print(len(newCards))


f.close()