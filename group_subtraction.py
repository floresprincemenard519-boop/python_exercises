first_number = float(input("Please input a number: "))
numbers_combined = 0

for num in range(9):
    numbers = float(input("Please input a number: "))
    numbers_combined += numbers
    
print(numbers_combined)