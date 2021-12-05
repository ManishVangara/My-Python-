import random

def computer_guess(x):
    low = 1 
    high =  x 
    feedback = ""
    while feedback != "C" :
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high (H), too low (L), or Correct (C)??")
        
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
    print(f'Finally! The computer guessed your number, {guess}, correctly!')


x = int(input("Please enter a number of your choice: "))
computer_guess(x)
