def collatz(number):
    if number % 2==0:
        print(number//2)
        return number // 2
    elif number % 2==1:
        result=(3*number+1)
        print(result)
        return result
    

print("Enter an integer: ")

try:
    return_value=collatz(int(input()))
    while return_value !=1:
        return_value=collatz(return_value)
except ValueError:
    print("You must enter an integer")
    

    