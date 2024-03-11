number = 10
max_guesses = 5
guesses_left = max_guesses

print("I'm thinking of a number...")

while guesses_left > 0:
    guess = input(f"What number am I thinking of? You have {guesses_left} guesses remaining.")

    if guess.lower() == 'q':
        print(f"Quitting the game. The number was {number}. Thanks for playing")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
        continue
    
    guesses_left -= 1

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! Your guess was too low.")
    else:
        print("Sorry! Your guess was too high.")

    if guesses_left == 0:
        print(f"Sorry, you've used all your guesses. The number was {number}.")