# Program to find the max in two numbers
print(max(10, 23))
print(max(10, 23, 45))
print(max(10, 23, 45, -1, -2, 100, 222.22, 87.34))

# TypeError: '>' not supported between instances of 'str' and 'int'
# which means string and integer cannot be compared
# print(max(10, 23, 45, -1, -2, 100, 1, "Pramod"))