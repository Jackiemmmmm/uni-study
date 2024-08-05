# Question1


# product_code = "377B"
# product_name = "Beef Liquid Stock"
# product_size = "250mL"
# product_price = 2.15

# print(product_code + ': ' + product_name + ', ' + product_size)

# print(product_name + ', ' + product_size + ', $' + str(product_price))

# print('{0}: {1}, {2}'.format(product_code, product_name, product_size))

# print('{0}, {1}, ${2}'.format(product_name, product_size, product_price))



# Question2


# COST_PER_COW = 30
# COST_PER_DUCK = 5
# COST_PER_CHICK = 3

# purchaseCow = int(input("Enter number of cows to purchase: "))
# purchaseDuck = int(input("Enter number of ducks to purchase: "))
# purchaseChick = int(input("Enter number of chicken to purchase: "))

# costCow = COST_PER_COW * purchaseCow
# costDuck = COST_PER_DUCK * purchaseDuck
# costChick = COST_PER_CHICK * purchaseChick
# totalCost = costCow + costDuck + costChick

# print("Cost:")
# print("{0} cow = {1} grassies".format(purchaseCow, costCow))
# print("{0} duck = {1} grassies".format(purchaseDuck, costDuck))
# print("{0} chick = {1} grassies".format(purchaseChick, costChick))
# print("Total = {0} grassies".format(totalCost))



# Question3


# print('|{0:>10}|{1:^30}{2:<10}'.format('Faces', 'Name', 'Vertices'))
# print('{0:>10}{1:^30}{2:<10}'.format(4, 'Tetrahedron', 4))
# print('{0:>10}{1:^30}{2:<10}'.format(6, 'Cube', 8))
# print('{0:>10}{1:^30}{2:<10}'.format(8, 'Octahedron', 6))
# print('{0:>10}{1:^30}{2:<10}'.format(12, 'Dodecahedron', 20))
# print('{0:>10}{1:^30}{2:<10}'.format(20, 'Icosahedron', 12))



# Question4

print('|{0:<10}|{1:^30}|{2:>10}|'.format('Faces', 'Name', 'Vertices'))
print('|{0:<10}|{1:^30}|{2:>10}|'.format(4, 'Tetrahedron', 4))
print('|{0:<10}|{1:^30}|{2:>10}|'.format(6, 'Cube', 8))
print('|{0:<10}|{1:^30}|{2:>10}|'.format(8, 'Octahedron', 6))
print('|{0:<10}|{1:^30}|{2:>10}|'.format(12, 'Dodecahedron', 20))
print('|{0:<10}|{1:^30}|{2:>10}|'.format(20, 'Icosahedron', 12))