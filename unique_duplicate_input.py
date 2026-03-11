list = []

while True:
    try:
        numbers = float(input("Please input a number: "))
        if numbers in list:
            print("Duplicate")
            list.append(numbers)
        else:
            print("Unique")
            list.append(numbers)
    except ValueError:
        print("You inputed an invalid number. \nStopping the loop.")
        break