# print("Escape sequence:")
# print("\\n : Insert a newline.")
# print("\\t : Insert a tab.")
# print("\\\" : Insert a double quote character.")
# print("\\\' : Insert a single quote character.")
# print("\\\\ : Insert a backslash character.")

# fname = "John"
# lname = "Smith"
# age = 20
# gpa_score = 3.2
# print("Hi {0} {1}!".format(fname, lname))
# print("{1} {2} is {0} years old".format(age, fname, lname))
# print("His GPA score is {0:.2f}".format(gpa_score))
# # :.2f用于格式化浮点数，保留两位小数。例如，如果你有一个浮点数3.14159，使用:.2f将其格式化为3.14。
# print("Formatted GPA score: {:.2f}".format(gpa_score))

# # 扩展用法:
# # :.3f将保留三位小数
# print("Three decimal places: {:.3f}".format(gpa_score))
# # :.1f将保留一位小数
# print("One decimal place: {:.1f}".format(gpa_score))

# # 对于字符串，format可以用来插入字符串，调整对齐方式等。
# # 例如，使用:<10s将字符串左对齐，并填充至少10个字符宽度。
# name = "Alice"
# print("Left aligned name: {:<10s}".format(name))
# # 使用:>10s将字符串右对齐，并填充至少10个字符宽度。
# print("Right aligned name: {:>10s}".format(name))
# # 使用:^10s将字符串居中对齐，并填充至少10个字符宽度。
# print("Center aligned name: {:^10s}".format(name))


# # 对于整数，可以使用类似的格式化方法。
# # :04d用于整数，保证至少有4位数字，不足部分用0填充。
# number = 42
# print("Zero padded number: {:04d}".format(number))
# # :+表示显示符号，对于正数显示+，负数显示-。
# print("Signed number: {:+d}".format(number))
# # format 方法还可以用来设置数字的进制表示。例如，使用:x可以将整数格式化为十六进制。
# hex_number = 255
# print("Hexadecimal: {:x}".format(hex_number))
# # 使用:o可以将整数格式化为八进制。
# oct_number = 255
# print("Octal: {:o}".format(oct_number))
# # 使用:b可以将整数格式化为二进制。
# bin_number = 255
# print("Binary: {:b}".format(bin_number))

# # format 还可以用来设置数字的千位分隔符，例如，使用:,可以在数字中添加逗号作为千位分隔符。
# large_number = 1000000
# print("Formatted with commas: {:,}".format(large_number))

# # 对于浮点数，除了可以设置小数点位数外，还可以使用%来将浮点数转换为百分比形式。
# percentage = 0.12345
# print("Percentage: {:.2%}".format(percentage))

# # format 方法也支持嵌套使用，可以在一个format调用中完成多个变量的格式化。
# name = "Bob"
# age = 30
# print("Name: {name}, Age: {age}".format(name=name, age=age))

# 算术运算符示例
# a = 10
# b = 3

# # 加法
# print("加法: a + b =", a + b)

# # 减法
# print("减法: a - b =", a - b)

# # 乘法
# print("乘法: a * b =", a * b)

# # 除法
# print("除法: a / b =", a / b)

# # 整除
# print("整除: a // b =", a // b)

# # 取余
# print("取余: a % b =", a % b)

# # 幂运算
# print("幂运算: a ** b =", a ** b)


# DISCOUNT_ITEMS = 3
# DISCOUNT_COST = 20
# NORMAL_COST = 10

# items = int(input('Please Input Items: '))

# getItemModules = items % DISCOUNT_ITEMS
# print(getItemModules)
# getItemFloorDivision = items // DISCOUNT_ITEMS
# print(getItemFloorDivision)
# getTotalCost = getItemFloorDivision * DISCOUNT_COST + getItemModules * NORMAL_COST

# print('{1} items cost {0}'.format(getTotalCost, items))


# lecture quiz


# 1

# subject_code = "CSCI111"
# subject_mark = 80
# subject_grade = "D"

# result = "Subject result: " \
#   + subject_code \
#   + " mark " + str(subject_mark) \
#   + " grade " + subject_grade 

# print(result)


#2

# print('Welcome to Unimovies!')
# print('Thursday July 30 at 7.15pm: \"Inside Out\"')


#3

# first_name = input('Enter first name: ')
# last_name = input('Enter last name: ')
# age = input('Enter age: ')
# gpa_score = input('Enter GPA score: ')
# print('Name: {0} {1}'.format(first_name, last_name))
# print('{0} {1} is {2} years old'.format(first_name, last_name, age))
# print('GPA score: {0:.2f}'.format(float(gpa_score)))


#4

# print('Alkali metals: \n')

# print('{0:<15}{1:<10}{2:^25}{3:>15}'.format('Element', 'Symbol', 'Atomic number', 'Atomic weight'))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Lithium', 'Li', 3, 6.94))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Sodium', 'Na', 11, 22.99))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Potassium', 'K', 19, 39.098))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Rubidium', 'Rb', 37, 85.468))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Caesium', 'Cs', 55, 132.905))
# print('{0:<15}{1:<10}{2:^25}{3:>15.4f}'.format('Francium', 'Fr', 87, 223))


#5

# first_name = input('Enter first name: ')
# last_name = input('Enter last name: ')
# age = input('Enter age: ')
# gpa_score = input('Enter GPA score: ')

# print('{0:<15}{1:>25}'.format('Name:', first_name + ' ' + last_name))
# print('{0:<15}{1:>25}'.format('Age:', age))
# print('{0:<15}{1:>25}'.format('GPA score:', gpa_score))
