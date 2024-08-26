# Quiz
# Question 1

# i = 0
# while i < 10:
#     print(i)
#     i += 1


# Question 2

# i = 9
# while i >= 0:
#     print(i)
#     i -= 1


# Question 3

# i = 0
# while i < 10:
#     print("5 x {0} = {1}".format(i, i * 5))
#     i += 1


# Question 4

# i = 0

# while i < 11:
#     print("{0} + {1} = 10".format(i, 10 - i))
#     i += 1


# Question 5

# i = 0
# while i <= 10:
#     if i == 10:
#         print(i, end=".")
#     elif i % 2 == 0:
#         print(i, end=", ")
#     i += 1


# Question 6

# startNum = int(input("Enter start number: "))
# endNum = int(input("Enter end number: "))

# print("\nEquations:")
# i = startNum
# while i < endNum + 1:
#     print("{0} + {1} = {2}".format(i, i, i + i))
#     i += 1


# Question 7

# continueLoop = True

# while continueLoop:
#     inputSomething = input("Enter something (or q to quit): ")
#     if inputSomething == "q" or inputSomething == "quit":
#         print("Goodbye!")
#         continueLoop = False
#     else:
#         print("You have entered: {0}\n".format(inputSomething))


# Question 8

# continueLoop = True

# while continueLoop:
#     inputPositiveInteger = int(input("Enter a positive integer: "))
#     if inputPositiveInteger > 0:
#         print("You have entered: {0}".format(inputPositiveInteger))
#         continueLoop = False
#     else:
#         print("")


# Question 9

# continueLoop = True
# oddCount = 0
# evenCount = 0

# while continueLoop:
#     inputSomething = input("Enter an integer (or q to quit): ")
#     if inputSomething == "q" or inputSomething == "quit":
#         print("You have entered {0} even numbers".format(evenCount))
#         print("You have entered {0} odd numbers".format(oddCount))
#         continueLoop = False
#     else:
#         if int(inputSomething) % 2:
#             oddCount += 1
#         else:
#             evenCount += 1


# Question 10

# i = 0

# while i < 10:
#     getChoice = input("Would you like green eggs and ham? (Y/N): ")
#     if getChoice == "Y":
#         i = 10
#         print("That's a smart choice!")
#     else:
#         if i == 9:
#             print("Oh well, you don't know what you're missing!")
#         i += 1

