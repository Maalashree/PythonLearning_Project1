# Factorial
import math
import math

n = 5
factorial = 1
# result = math.factorial(5)
# print(result)
# range(1,10) #1-9

# while n > 0:
#     factorial = factorial * n
#     n = n - 1


for i in range(1, n + 1):
    factorial *= i


print(factorial)

### Practiced code ###

# num = int(input("Enter a number \n"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
#     print(factorial)
#
# print("Factorial of", num , "is", factorial)

# num = int(input("Enter a number \n"))
# original_num=num
# factorial = 1
# while (num > 0):
#     factorial = factorial * num
#     num = num - 1
#
# print("Factorial of ", original_num, "is", factorial)