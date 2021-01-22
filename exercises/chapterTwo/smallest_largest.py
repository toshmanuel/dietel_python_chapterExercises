# (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.
int_a = int(input('enter first value \n'))
int_b = int(input('enter second input \n'))
int_c = int(input('enter third number \n'))

minimum = int_a
maximum = int_a

if minimum > int_b:
    minimum = int_b
if minimum > int_c:
    minimum = int_c
if maximum < int_b:
    maximum = int_b
if maximum < int_c:
    maximum = int_c

print('minimum of the three numbers is: ', minimum)
print('maximum of the three numbers is: ', maximum)
