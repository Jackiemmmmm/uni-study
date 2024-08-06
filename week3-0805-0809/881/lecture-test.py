# Example 1-2

# items = int(input("Please Input Number of items: "))
# deliveryPost = input("Please Choose your post(S / R / E): ")

# itemCost = 3
# postage = 10

# if items > 50:
#     itemCost = 2
#     postage = 0

# if deliveryPost == "R":
#     postage = 15
# elif deliveryPost == "E":
#     postage = 20

# totalCost = itemCost * items + postage

# print("{0} x {1} + {2} = {3}".format(items, itemCost, postage, totalCost))


# Example 3

GRADE_A = 80
GRADE_B = 60
GRADE_C = 40

mark = int(input("Please enter the mark: "))

grade = "D"

if mark >= GRADE_A:
    grade = "A"
elif mark >= GRADE_B:
    grade = "B"
elif mark >= GRADE_C:
    grade = "C"

print("Mark: {0}, Grade: {1}".format(mark, grade))
