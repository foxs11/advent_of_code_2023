import re
from  word2number import w2n


# f = open('01/input01.txt', 'r')

# input = f.readlines()

# numbers = []

# for i in input :
#     match = re.search(r'\d', i)
#     print(match.group())

#     match2 = re.search(r'\d', i[::-1])
#     print(match2.group())

#     number = int(match.group() + match2.group())
#     # print(number)

#     numbers.append(number)

# number = 0

# for i in numbers:
#     number = number + i

# print(number)
# f.close


number_words = {
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    }

f = open('01/input01.txt', 'r')

input = f.readlines()

numbers = []

for i in input :
    n = i
    print(n)
    for number_word in number_words:
        if number_word in n:
            n = n.replace(number_word, number_word[0] + str(w2n.word_to_num(number_word)) + number_word[-1])
    print(n)
    match = re.search(r'\d', n)
    print(match.group())

    match2 = re.search(r'\d', n[::-1])
    print(match2.group())

    number = int(match.group() + match2.group())
    # print(number)

    numbers.append(number)

number = 0

for i in numbers:
    number = number + i

print(number)
f.close