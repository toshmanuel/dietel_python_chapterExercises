int_input = int(input('Enter input (input should be a five(5) digits integer value: '))
if 10000 <= int_input <= 99999:
    divisor = 10000
    for counter in range(5):
        temp = int_input // divisor
        int_input = int_input % divisor
        print(temp, end=' ')
        divisor = divisor // 10
else:
    print('invalid input, try again.')
