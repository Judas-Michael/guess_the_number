import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    #'''Set the high and low values for the random number'''
	while True:
		try:
			high = int(input("What is the highest secret number "))
			low = int(input("What is the lowest secret number "))
			return low,high
		except ValueError:
			print('Numbers only please') #validates as numeric
		
	
   


def generate_secret(low, high):
    #'''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    #'''get user's guess'''
	
	while True: #repeats until number is given 
		try: 
			guess = int(input('Guess the secret number? '))
			return guess
		except ValueError:
			print('Numbers only please') #validates value as numeric
		


def check_guess(guess, secret):
   # '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high

		
def validate(guess):
	if guess == int:
		return
	else:
		print("That is not a number") 

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

#Maybe do an entire new class as 'Validate' as opposed to individual validation?