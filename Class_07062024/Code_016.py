# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.
# Conversion of str to int

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int -> ? int()
result = int(num1)+int(num2)
result2=int(num1+num2)
print(result)
print(result2)

#  + operator-> In case of int performs sum operation
#  + operator-> In case of str performs concat
# int to str -> str()
# str to int -> int()
print(type(num1))
print(type(int(num1)))
print(type(result2))