futureValue=float(input('Enter the desired future value: '))
rate=float(input('Enter the annual interest rate: '))
years=int(input('Enter the number of years the money will grow: '))

presentValue=futureValue/(1.0+rate)**years

print('You will need to deposit this amount: $',format(presentValue, ',.2f'))