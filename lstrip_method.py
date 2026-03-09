# lstrip() example function
string = "   What a beautiful world! Helloooooo!"
# print(string.lstrip())
spaceless_string = ""
non_space_detected = False
# remove spaces without using lstrip()

# check if the characters in string is space or not
# if character is space then remove it from the string
# if encountered a non space dont remove spaces further 
for char in string:
    if char != " ":
        spaceless_string += char
        non_space_detected = True

print(spaceless_string)