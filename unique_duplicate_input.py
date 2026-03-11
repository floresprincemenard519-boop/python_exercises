# get numbers using loops
# if its unique print unique and ask again
# if its not then say duplicate then ask again
# ask untill there is an error cause invalid input
list = []
while True:
    numbers = float(input("Please input a number: "))
    if numbers in list:
        print("Duplicate")
        list.append(numbers)
    else:
        print("Unique")
        list.append(numbers)