# Strings
# Bunch of Char
# '', "" , """
name = 'Harry'
print(name)
name = "Harry"
print(name)
name = """Harry, Is is Good person
He love to walk alone, He has a dog
....
....

....
"""
print(name)

# Raw String...Dir path can be mentioned either in single/double quotes
dir = r'C:\nomedir\some dir'
print(dir)
dir1 = r"d:\checkfile\some"
print(dir1)
dir2 = "e:\checkfile\some"
print(dir2)

# Format of the String
first_name = "Harry"
last_name = "Potter"
print(first_name + " " + last_name)
print(first_name, last_name)
# f -> formatting - it will replace the values of the variables
# {} -> placeholders
# print('Your Full name is {first_name} {last_name}')
print(f'Your Full name is {first_name} {last_name}')
print('Your Full name is', first_name, last_name )
