import random

secret_number=random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")

for guess in range(1, 5):
    print('Enter a number to guess: ')
    guessNumber=int(input())

    if guessNumber<secret_number:
        print('YOur guess is too low')
    elif guessNumber>secret_number:
        print('Your guess is too high')
    else:
        break

if guess==secret_number:
    print('Good JOb! You guessed my number in {guesses} guesses!'.format(guesses=str(guess)))
else:
    print('Nope the number I was thinking of was {number}'.format(number=str(secret_number)))