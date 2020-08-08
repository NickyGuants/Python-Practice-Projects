'''A program that asks a user to enter the number of 
packages sold/purchased and returns the amount of discount
and the total amount after the discount
'''

price_of_package=99

number_of_packages_purchased=int(input("Enter the number of packages purchased: "))
total_price=price_of_package*number_of_packages_purchased


if number_of_packages_purchased<10:
    discount=total_price*0.0
    print("Sorry, No discount for packages below 10.")
elif number_of_packages_purchased<20:
    discount=total_price*0.1
elif number_of_packages_purchased<50:
    discount=total_price*0.2
elif number_of_packages_purchased<100:
    discount=total_price*0.3
else:
    discount=total_price*0.4

total_amount_after_discount=(number_of_packages_purchased*price_of_package-discount)

print("The amount of discount is {discount} and the total amount of the purchase after discount is {total}".format(discount=discount, total=total_amount_after_discount))
