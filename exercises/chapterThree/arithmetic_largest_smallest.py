
grade = 1
max_temp = int(input('enter value 1: '))
min_temp = max_temp
total = min_temp
product = min_temp
for grade in range(2, 5):
    number = int(input(f'enter value { grade} '))
    number2 = number
    if number >= max_temp:
        max_temp = number
    if number2 <= min_temp:
        min_temp = number2
    total += number
    product *= number
print('total= ', total)
print("average= ", total / grade)
print('product= ', product)
print('maximum value is ', max_temp)
print('minimum value is ', min_temp)
