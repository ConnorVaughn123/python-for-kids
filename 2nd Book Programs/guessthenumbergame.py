# guess the number game
secret_number = 32
n = input('Guess the secret number between 1 and 100: ')
n = int(n) # convert user input into a integer
if n == secret_number:
    print('You got it!')
else:
    # not equal to secret number so check if higher or lower
    if n > secret_number:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
print('Thanks for playing') # this is done in all cases
