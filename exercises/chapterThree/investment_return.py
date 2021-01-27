amount_invested = int(input('Enter amount you want to invest: '))
rate = 0.09
years = 1

for returns in range(30):
    amount = amount_invested * (1 + rate) ** years
    print(f"{amount:.2f}")
    years += 1
