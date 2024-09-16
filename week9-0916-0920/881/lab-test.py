# Question 1


# class Staff:

#     def __init__(self, staff_number, first_name, last_name, email):
#         self.staff_number = staff_number
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email


# Question 2


# class Staff:

#     def __init__(self, staff_number, first_name, last_name, email):
#         self.staff_number = staff_number
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

#     def __str__(self):
#         return (
#             self.staff_number
#             + ", "
#             + self.first_name
#             + ", "
#             + self.last_name
#             + ", "
#             + self.email
#         )


# staffObj1 = Staff("100001", "John", "Lee", "jl123@gmail.com")
# staffObj2 = Staff("100002", "Mary", "Zheng", "maryz@gmail.com")
# staffObj3 = Staff("100003", "Cindy", "Wilson", "cw456@hotmail.com")


# Question 3


# class Staff:

#     def __init__(self, staff_number, first_name, last_name, email):

#         self.staff_number = staff_number
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

#     def print_details(self, width):
#         print("-" * width)
#         print("| {0:<{1}} |".format("Staff number: " + self.staff_number, width - 4))
#         print("| {0:<{1}} |".format(self.first_name + " " + self.last_name, width - 4))
#         print("| {0:<{1}} |".format(self.email, width - 4))
#         print("-" * width)


# staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
