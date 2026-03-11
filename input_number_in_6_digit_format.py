# get inputed number from 1 to 1000
# add 0 in front to make it into 6 digit number
number = float(input("Please give a number ranging from 0 to 1000: "))
while len(number) != 4 or len(number) > 4:
    print()