string = "i should have a capital letter at the beginning."

# how capitalize() works
print(string.capitalize())

# how capitalize() works without capitalize() method

if string[0].islower():
    char = string[0].upper()
    print(char + string[1:])
else:
    print(string)
