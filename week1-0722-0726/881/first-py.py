
# # My first Python program
# print("PPP   Y   Y  TTTTT  H  H   OO   N   N")
# print("P  P   Y Y     T    H  H  O  O  NN  N")
# print("PPP     Y      T    HHHH  O  O  N N N")
# print("P       Y      T    H  H  O  O  N  NN")
# print("P       Y      T    H  H   OO   N   N")

# # print blank lines
# print()
# print()

# # print greetings
# print("Welcome to Python - Class of 2024!")

# ######################

# # print hello and greeting
# print("Hello World!")
# print('Welcome to Python!')

# ######################

# # print hello and greeting and silly stuff :-)
# print('Hello World!', end=" frog ")
# print("Welcome to Python!", end=" cat ")
# print("How are you?")

# ######################

# # What is wrong with this code?
# # print(Hello World!)

# ######################

# # ALWAYS use variables with meaningful names and correct data types

# # string data type: using either double quote or single quote
# first_name = "John"
# last_name = 'Smith'

# print(first_name)
# print(last_name)

# # display data type
# print(type(first_name))
# print(type(last_name))


# if type(first_name) == str:
#     print("first_name is a string.")
# else:
#     print("first_name is not a string.")



# ######################

# # integer data type: whole numbers
# age = 20
# temperature = -5
# credit_point = 6

# print(age)
# print(temperature)
# print(credit_point)

# # display data type
# print(type(age))
# print(type(temperature))
# print(type(credit_point))

# ######################

# # float: decimal numbers
# price = 30.5
# interest_rate = 3.18

# print(price)
# print(interest_rate)

# # display data type
# print(type(price))
# print(type(interest_rate))

# ######################

# # import the math module
# import math

# # some important math constants
# # do you know what are these?
# pi = math.pi
# e = math.e
# tau = math.tau

# print(pi)
# print(e)
# print(tau)

# # display data type
# print(type(pi))
# print(type(e))
# print(type(tau))

# ######################

# # boolean type: True or False

# virus_scan_completed = True
# virus_found = False

# print(virus_scan_completed)
# print(virus_found)

# # display data type
# print(type(virus_scan_completed))
# print(type(virus_found))

# temperature = -5
# temperature_negative = temperature < 0
# print(temperature_negative)

# temperature_positive = temperature > 0
# print(temperature_positive)

# ######################

# import datetime

# # get current date
# today_date = datetime.date.today()

# # US election date 2020
# us_election_2020 = datetime.date(2020, 11, 3)

# print(today_date)
# print(us_election_2020)

# print("Election date is " + str(us_election_2020))
# print("Election date is " + us_election_2020.strftime("%d-%b-%Y"))

# # display data type
# print(type(today_date))
# print(type(us_election_2020))



# if type(us_election_2020) == datetime.date:
#     print("us_election_2020 is a datetime.date.")
# else:
#     print("us_election_2020 is not a datetime.date.")


# ######################

# # date data type: year, month, day, hour, minute, second, microsecond

# import datetime

# current_date_time = datetime.datetime.now()

# christmas_2020 = datetime.datetime(2020, 12, 25)

# random_date_time = datetime.datetime(2000, 12, 20, 14, 20, 39, 555)

# print(current_date_time)
# print(christmas_2020)
# print(random_date_time)

# # display data type
# print(type(current_date_time))
# print(type(christmas_2020))
# print(type(random_date_time))

# ######################

# # string addition example

# # name details
# first_name = "John"
# last_name = "Smith"

# # use string addition to formulate the full name
# full_name = first_name + " " + last_name

# # display the full name
# print("My name is " + full_name + ".")

# ######################

# # String multiplication (with number)!

# # display some silly strings

# silly1 = "frog " * 7

# silly2 = 5 * " I am Sam "

# print(silly1)

# print(silly2)

# ######################

# # Get input from the user

# # ask the user to enter first name and last name
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # use string addition to formulate the full name
# full_name = first_name + " " + last_name

# # display the full name
# print("My name is " + full_name + ".")

# ######################

# # Get input from the user

# # Ask the user to enter 3 subjects
# print("You must choose 3 subjects.")
# print()

# subject1 = input("Enter the 1st subject: ")
# subject2 = input("Enter the 2nd subject: ")
# subject3 = input("Enter the 3rd subject: ")

# # Display subjects
# print()
# print("You have chosen: " + subject1 + ", " + subject2 + ", " + subject3 + ".")

# # Display subjects - this is clearer to read
# print()
# print('You have chosen: ' 
#   + subject1 + ", " 
#   + subject2 + ", " 
#   + subject3 + "."
# )

######################

# Convert number into string

# A program to display the favorite number

# favorite number
# fav_number = 7

# what is wrong with this code?
# print("My favorite number is " + fav_number)


# # display favorite number
# print("My favorite number is " + str(fav_number))

# ######################

# Ask the user to enter 2 integers and display the sum
# number1 = input("Enter the 1st integer: ")
# while True:
#     number2 = input("Enter the 2nd integer: ")
#     if number2.isdigit() or (number2.startswith('-') and number2[1:].isdigit()):
#         break
#     else:
#         print("Please enter a valid integer.")

# # calculate the sum
# number_sum = int(number1) + int(number2)

# # display the sum - what is wrong with this code?
# print("The sum is " + str(number_sum))

# ######################

# # Ask the user to enter 2 integers and display the sum
# user_input1 = input("Enter the 1st integer: ")
# number1 = int(user_input1)

# user_input2 = input("Enter the 2nd integer: ")
# number2 = int(user_input2)

# # calculate the sum
# number_sum = number1 + number2

# # display the sum
# print("The sum is " + str(number_sum))

# # display the sum - this is clearer
# print("The sum of " 
#   + str(number1)
#   + " and " 
#   + str(number2)
#   + " is "
#   + str(number_sum)
# )

# ######################

# # Ask the user to enter 2 decimal numbers and display the sum
# user_input = input("Enter the 1st number: ")
# number1 = float(user_input)

# user_input = input("Enter the 2nd number: ")
# number2 = float(user_input)

# # calculate the sum
# number_sum = number1 + number2

# # display the sum
# print("The sum of " 
#   + str(number1)
#   + " and " 
#   + str(number2)
#   + " is "
#   + str(number_sum)
# )

# ######################

# # convert integer to string

# age = 20

# # this is wrong
# #print("I am " + age + " years old")

# # this is correct
# print("I am " + str(age) + " years old")

# ######################

# # convert float to string

# interest_rate = 3.18

# # this is wrong
# #print("The interest rate is " + interest_rate + "%")

# # this is correct
# print("The interest rate is " + str(interest_rate) + "%")

######################

# import datetime

# # ask the user enter dob in DD/MM/YYYY format
# user_input = input("Enter your dob (DD/MM/YYYY): ")

# # convert string type to date type
# date_format = '%d/%m/%Y'  
# dob = datetime.datetime.strptime(user_input, date_format).date()

# # convert date to string
# print("Your dob is " + dob.strftime("%d/%b/%Y"))
# print("Your dob is " + dob.strftime("%d-%m-%Y"))

# ######################

# import datetime

# # ask the user enter dob in DD/MM/YYYY format
# user_input = input("Enter your dob (DD/MM/YYYY): ")

# # convert string type to date type
# date_format = '%d/%m/%Y'  
# dob = datetime.datetime.strptime(user_input, date_format)

# # convert date to string
# print("Your dob is " + dob.strftime("%d-%b-%Y"))
# print("Your dob is " + dob.strftime("%d-%m-%Y %H:%M:%S.%f"))

# ######################




print('Thursday July 30 at 7.15pm: "Inside Out"')