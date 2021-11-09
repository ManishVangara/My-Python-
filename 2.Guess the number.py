import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number between 1 and {} : ".format(x)))
        if guess < random_number :
            print("Sorry, guess again. Too low")
        elif guess > random_number :
            print(f"Sorry guess again. Too high")
    
    print(f"Yay, congrats. You guessed the number {random_number} correctly.")


guess(2000)