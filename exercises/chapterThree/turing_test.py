message = input("What is your problem?: ")
second_message = input('Have you had this problem before (yes or no)?: ')
if second_message.lower() == 'yes':
    print("Well, you have it again")
if second_message.lower() == 'no':
    print('Well, you have it now')
