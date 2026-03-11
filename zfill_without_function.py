# get number in str
# if len of str less than parameter add 0 to front
# print

numbers = '1231321'
zfill_parameter = 10

if len(numbers) != zfill_parameter:
    print((zfill_parameter - len(numbers)) * '0' + numbers)