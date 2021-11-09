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


computer_guess(20000)


# def computer_guess(x):
#     low = 1 
#     high =  x 
#     feedback = ""
#     while feedback != "C" :
#         if low != high :
#             guess = random.randint(low,high)
#         else :
#             guess = low         # could also be high b/c low = high
#         feedback = input(f"Is {guess} too high (H), too low (L), or Correct (C)")
#         if feedback == "H":
#             high = guess - 1
#         elif feedback == "L":
#             low = guess + 1
#     print(f'Yay! The computer guessed your number, {guess}, correctly!')