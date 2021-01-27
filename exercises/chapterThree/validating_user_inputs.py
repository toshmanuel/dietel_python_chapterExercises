# (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.

passes = 0
failures = 0
counter = 1

result = 0
for student in range(10):
    result = int(input(f'enter results for student {counter} (1=pass or 2=fail): '))
    while result != 1 and result != 2:
        print('enter value again')
        result = int(input(f'enter results for student {counter} (1=pass or 2=fail): '))
    if result == 1:
        passes += 1
    if result == 2:
        failures += 1
    counter += 1
print(passes)
print(failures)
