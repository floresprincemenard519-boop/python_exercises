
list = []

while True:
    try:
        numbers = float(input("Please input a number: "))
        list.append(numbers)
    except ValueError:
        for num in sorted(list):
            print(num, end=" ")
        break