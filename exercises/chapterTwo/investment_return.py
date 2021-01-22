rate = 7/100
principal = int(input('enter amount to invest: '))
number_of_years = int(input('enter number of years to invest: '))
amount = principal * (1 + rate) ** number_of_years
print('amount after', number_of_years, 'is', amount)
