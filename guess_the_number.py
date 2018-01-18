import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'

def validate_input(entry, message):
    # Attempt to parse user entry to INT. Handle value error
    # with while loop. Loop message until an int is entered.
    while True:
        try:
            entry = int(entry)
        except ValueError:
            print('Invalid entry. Use integers only.')
            entry = input(message)
            continue
        else:
            break

    return entry


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    message = 'Guess the secret number? '
    guess = validate_input(input(message), message)
    return guess


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()
