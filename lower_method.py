string = "ABCDEFG HI! EHHEHE"
second_string = "AbCdEfG Hi! HeHeHe"
lower_string = ""
# how lower() works
print(string.lower())

# how lower() works without lower() method
# can't do without lower() method cause dont know how convert that to numbers then to acii
#  but i discovered i can use swapcase so im gonna use that 
for char in second_string:
    if char.isupper():
        lower_string += char.swapcase()
    else:
        lower_string += char

