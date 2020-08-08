'''A program that asks the user to enter he weight of a package and displays the shipping charges'''

weight_of_package=int(input("Enter the weight of package in pounds: "))
if weight_of_package<=2:
    shipping_charges=weight_of_package*1.5
elif weight_of_package<=6:
    shipping_charges=weight_of_package*3.0
elif weight_of_package<=10:
    shipping_charges=weight_of_package*4.0
else:
    shipping_charges=weight_of_package*4.75


print("Your shipping charges are: ${charges}".format(charges=shipping_charges))