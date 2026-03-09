string = "   What a beautiful world! Helloooooo!"
prefix_to_remove = "   W"
# how removeprefix() works
print(string.removeprefix('   W'))

# same functionality without using removeprefix()
# find the index to remove and exclude it from the string
string = string[len(prefix_to_remove):]
print(string)