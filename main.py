import random

hidden_number = random.randint(1, 10)
print("""-------------------------Guess the number-------------------------
You will have only 3 chances""")
no_of_guess = 0
guess = 0


def takinginput():
    try:
        global guess
        guess = int(input('Enter your guess '))
    except Exception:  # preventing errors
        print('Try entering a numeric value')
        takinginput()  # loop if data provided by user isn't numeric


while True:
    takinginput()
    no_of_guess += 1
    if guess > hidden_number:
        print('Your guess is too high. Guess no ' + str(no_of_guess))
    if guess < hidden_number:
        print('Your guess is too low. Guess no ' + str(no_of_guess))
    if guess == hidden_number:
        print('You guessed correct in ' + str(no_of_guess) + ' guess the correct number was ' + str(hidden_number))
        break
    if no_of_guess == 3:
        print('You could not guess the correct number.!' + f' The number was {hidden_number}')
        break

quit()  # be idle friendly by quitting the programme
