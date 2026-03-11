string = "What a beautiful world! Helloooooo!    "
string = list(string)

for index in range(len(string)-1, -1, -1):
    if string[index] == ' ':
        string.pop(-1)
    else:
        break

# to show that the spaces are removed
print(string)

for char in string:
    print(char, end="")