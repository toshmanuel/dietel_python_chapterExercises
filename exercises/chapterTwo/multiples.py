multiples = int(input("enter first number "))
number = int(input('enter second number '))

if number % multiples == 0:
    print(multiples, 'is a multiple of ', number)
else:
    print(multiples, 'is not a multiple of ', number)
