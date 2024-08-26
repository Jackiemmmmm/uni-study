# Question 1

# i = 2
# while i < 11:
#     print("{0:>2} + {0:>2} = {1:>2}".format(i, i + i))
#     i += 2


# Question 2

# i = 1
# while i < 10:
#     if i < 9:
#         print(i, end="; ")
#     else:
#         print(i, end=".")
#     i += 2

# Question 3

# continueToEnter = True
# count = 0
# sum = 0
# even = 0
# odd = 0
# positive = 0
# negative = 0

# while continueToEnter:
#     inputValue = input("Enter an integer or q to quit: ")
#     if inputValue == "q" or inputValue == "quit":
#         break
#     inputInt = int(inputValue)
#     count += 1
#     sum += inputInt
#     if inputInt % 2:
#         odd += 1
#     else:
#         even += 1
#     if inputInt > 0:
#         positive += 1
#     elif inputInt < 0:
#         negative += 1

# print("\nSummary information:")
# print("You have entered {0} integers.".format(count))
# print("The sum of these numbers is {0}.".format(sum))
# print("There are {0} even numbers.".format(even))
# print("There are {0} odd numbers.".format(odd))
# print("There are {0} positive numbers.".format(positive))
# print("There are {0} negative numbers.".format(negative))


# Question 4

# list = []
# continueToEnter = True

# while continueToEnter:
#     inputValue = input("Enter an integer or q to quit: ")
#     if inputValue == "q" or inputValue == "quit":
#         break
#     inputInt = int(inputValue)
#     list.append(inputInt)

# print("Before insertion sort: {0}".format(list))


# def sortList(array):
#     length = len(array)
#     for value in range(1, length):
#         innerKey = value
#         while innerKey > 0 and array[innerKey] > array[innerKey - 1]:
#             newValue = array[innerKey]
#             array[innerKey] = array[innerKey - 1]
#             array[innerKey - 1] = newValue
#             innerKey -= 1


# sortList(list)
# print("After insertion sort: {0}".format(list))


# Question 5

# 2, 8, 4, 10, 6, 0, 12