# Question 1


# def triple(sentence):
#     newStr = ""
#     for value in sentence:
#         newStr += value * 3
#     return newStr


# Question 2


# def triple(sentence):
#     result = ""
#     for i in sentence:
#         result += i * 3
#     return result


# inputValue = input("Enter a sentence: ")

# result = triple(inputValue)

# print("Triple effect: {0}".format(result))


# Question 3


# def next_number(int):
#     if int % 2:
#         return 2 * int + 2
#     else:
#         return 3 * int + 1


# Question 4


def next_number(int):
    if int % 2:
        return 2 * int + 2
    else:
        return 3 * int + 1


initNumber = int(input("Enter the initial number: "))

print("Sequence:")
index = 0
becomesNumbers = initNumber
isContinue = True
while isContinue:
    print("Step {0}: {1}".format(index, becomesNumbers))
    if becomesNumbers > 100:
        isContinue = False
    becomesNumbers = next_number(becomesNumbers)
    index += 1
