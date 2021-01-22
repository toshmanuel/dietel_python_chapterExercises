int_a = int(input('enter number\nnote: number should be a five digit number\n'))
if 10000 <= int_a <= 99999:
    fifth_number = int_a % 10
    int_a = int_a // 10
    fourth_number = int_a % 10
    int_a = int_a // 10
    third_number = int_a % 10
    int_a = int_a // 10
    second_number = int_a % 10
    int_a = int_a // 10
    print(int_a, ' ', second_number, ' ', third_number, ' ', fourth_number, ' ', fifth_number)
