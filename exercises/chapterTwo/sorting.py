int_a = int(input('enter first value \n'))
int_b = int(input('enter second input \n'))
int_c = int(input('enter third number \n'))

minimum = int_a

if int_a >= int_b:
    if int_b >= int_c:
        print(int_c, int_b, int_a)
    elif int_c >= int_b and int_c >= int_a:
        print(int_b, int_a, int_c)
    else:
        print(int_b, int_c, int_a)


if int_a <= int_b:
    if int_b <= int_c:
        print(int_a, int_b, int_c)
    elif int_c <= int_b and int_c <= int_a:
        print(int_c, int_a, int_b)
    else:
        print(int_a, int_c, int_b)














