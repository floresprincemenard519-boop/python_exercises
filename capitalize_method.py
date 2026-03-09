string = "i should have a capital letter at the beginning."
second_string = "Im the second ehhhehehe."

# how capitalize() works
print(string.capitalize())

# how capitalize() works without capitalize() method

if second_string[0].islower():
    char = second_string[0].upper()
    print(char + second_string[1:])
else:
    print(second_string)
