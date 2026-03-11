# get a string
# remove space in the right side

string = "What a beautiful world! Helloooooo!    "

for index in range(len(string)-1, -1, -1):
    if string[index] == ' ':
        print('', end='')
    elif string[index] == ' ':
        break
    print(string[index], end='')