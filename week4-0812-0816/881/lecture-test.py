# Question 1
# for value in range(2, 9):
#     print(value)


# Question 2
# for value in range(1, 10):
#     print('6 x {0} = {1}'.format(value, value * 6))


# Question 3
# inputNumber = int(input('Enter a number: '))

# for value in range(1, 10):
#     print('{0} x {1} = {2}'.format(inputNumber, value, inputNumber * value))


# Question 4
# for value in range(0, 11):
#     print('{0} + {1} = 10'.format(value, 10 - value))


# Question 5
# for value in range(0, 11):
#     if value != 10:
#         print(value, end=", ")
#     else:
#         print(value, end=".")


# Question 6
# sum = 0
# for value in range(2, 21):
#     sum += value
# print('The sum of 2 to 20 is {0}'.format(sum))


# Question 7
# sentence = input('Enter a sentence: ')

# for value in sentence:
#     print(value)


# Question 8
# username = input("Enter username: ")

# convertPassword = ""
# for value in username:
#     if value.lower() == "i":
#         convertPassword += "1"
#     elif value.lower() == "r":
#         convertPassword += "7"
#     elif value.lower() == "s":
#         convertPassword += "5"
#     elif value.lower() == "z":
#         convertPassword += "2"
#     else:
#         convertPassword += value
# print('Password is {0}'.format(convertPassword))


# Question 9
for value in range(0, 10):
    inputValue = input("Would you like green eggs and ham? (Y/N): ")
    if inputValue == "Y":
        break
