# def sum_part_numbers(schematic):
#     rows = len(schematic)
#     cols = len(schematic[0]) if rows > 0 else 0
#     sum_parts = 0

#     def is_symbol(char):
#         return char not in ".0123456789"  # Add other symbols if necessary

#     def is_valid_number(i, j):
#         # Check all eight adjacent positions for a symbol
#         for dx in [-1, 0, 1]:
#             for dy in [-1, 0, 1]:
#                 if dx == 0 and dy == 0:
#                     continue
#                 x, y = i + dx, j + dy
#                 if 0 <= x < rows and 0 <= y < cols and is_symbol(schematic[x][y]):
#                     return True
#         return False

#     def get_full_number(i, j):
#         # Extracts the full number starting from position (i, j)
#         num = ''
#         while j >= 0 and schematic[i][j].isdigit():
#             print(j)
#             j = j - 1
#         j = j + 1 
#         while j < cols and schematic[i][j].isdigit():
#             num += schematic[i][j]
#             j += 1
#         print(num)
#         return int(num)

#     i = 0
#     while i < rows:
#         j = 0
#         while j < cols:
#             # print(schematic[i][j])
#             if schematic[i][j].isdigit():
#                 # print(is_valid_number(i, j))
#                 if is_valid_number(i, j):
#                     sum_parts += get_full_number(i, j)
#                 # Skip the rest of the number
#                     while j < cols and schematic[i][j].isdigit():
#                         j += 1
#                 else:
#                     j += 1
#             else:
#                 j += 1
#         i += 1

#     return sum_parts

# f = open('03/input03.txt', 'r')
# input = f.readlines()
# rows = len(input) - 1
# columns = len(input[0]) - 1


# cleanLines = []

# for i in input:
#     i = i.replace("\n", "")
#     cleanLines.append(i)
#     print(i)


# print(sum_part_numbers(cleanLines))



# f.close()














def sum_part_numbers(schematic):
    rows = len(schematic)
    cols = len(schematic[0]) if rows > 0 else 0
    sum_parts = 0

    def is_symbol(char):
        return char not in ".0123456789"  # Add other symbols if necessary

    def is_valid_symbol(i, j):
        # Check all eight adjacent positions for a number
        multiply = 1
        num = 0
        dx = -1
        while dx <= 1:
            dy = -1
            while dy <= 1:
                if dx == 0 and dy == 0:
                    dy = dy + 1
                    continue
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and schematic[x][y].isdigit():
                    num = num + 1
                    multiply = multiply * get_full_number(x, y)
                    while j + dy < cols and schematic[x][j + dy].isdigit():
                        dy += 1
                dy += 1
            dx = dx + 1
        print(multiply)
        if num == 2:
            return multiply
        else:
            return 0

    def get_full_number(i, j):
        # Extracts the full number starting from position (i, j)
        num = ''
        while j >= 0 and schematic[i][j].isdigit():
            j = j - 1
        j = j + 1 
        while j < cols and schematic[i][j].isdigit():
            num += schematic[i][j]
            j += 1
        print(num)
        return int(num)

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            # print(schematic[i][j])
            if schematic[i][j] == "*":
                sum_parts = sum_parts + is_valid_symbol(i, j)
                # if is_valid_symbol(i, j):
                #     sum_parts += get_full_number(i, j)
                # # Skip the rest of the number
                #     while j < cols and schematic[i][j].isdigit():
                #         j += 1
                # else:
                j += 1
            else:
                j += 1
        i += 1

    return sum_parts

f = open('03/input03.txt', 'r')
input = f.readlines()
rows = len(input) - 1
columns = len(input[0]) - 1


cleanLines = []

for i in input:
    i = i.replace("\n", "")
    cleanLines.append(i)
    print(i)


print(sum_part_numbers(cleanLines))



f.close()