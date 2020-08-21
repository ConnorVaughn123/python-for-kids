# guess the number game v2
secret_number = 32
n = input('Guess the secret number between 1 and 100: ')
n = int(n) # convert user input into a integer
while not (n == secret_number):
    # not equal to secret number so check if higher or lower
    if n > secret_number:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
    # ask user for another guess
    n = input('Make another guess between 1 and 100: ')
    n = int(n)
print('You got it!')
