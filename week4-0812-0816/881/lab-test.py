# # Question 1 and Question 2

# items = int(input("Enter the number of items: "))
# postMethod = input('Enter shipping method (s/r/e): ')

# itemCost = 3
# postage = 10
# methodString = 'Standard'

# if postMethod == 'r':
#     postage = 15
#     methodString = 'Registered'
# elif postMethod == 'e':
#     postage = 20
#     methodString = 'Express'

# if items > 50:
#     itemCost = 2
#     postage = 0
#     if postMethod == 'r':
#         postage = 10
#     elif postMethod == 'e':
#         postage = 17


# totalCost = itemCost * items + postage

# print("\nReceipt:")
# print("{0} items x ${1} = ${2}".format(items, itemCost, items * itemCost))
# print("{0} post: ${1}".format(methodString, postage))
# print("Total: ${0}".format(totalCost))



# Question 3

firstInt = int(input('Enter the first integer: '))
secondInt = int(input('Enter the second integer: '))
thirdInt = int(input('Enter the third integer: '))
fourthInt = int(input('Enter the fourth integer: '))

min = firstInt
max = firstInt

if min > secondInt:
    min = secondInt
if min > thirdInt:
    min = thirdInt
if min > fourthInt:
    min = fourthInt

if max < secondInt:
    max = secondInt
if max < thirdInt:
    max = thirdInt
if max < fourthInt:
    max = fourthInt
    
print('\nThe minimum number is {0} and the maximum number is {1}.'.format(min, max))
