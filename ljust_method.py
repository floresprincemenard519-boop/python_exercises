# how ljust() works
string = "I should be 50 letters long, but I'm not."
print(string.ljust(50,"-"))

# how ljust() work without ljust() method
if len(string) != 50:
    print(string + "-" * (50 - len(string)))
else:
    print(string)