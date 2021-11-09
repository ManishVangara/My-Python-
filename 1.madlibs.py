# # string concatenation (aka how to put string together)

# youtuber = input("")

# # ways to concatenate 

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous person: ")

# METHOD 1

madlib = f"Computer Programming is so {adj}! It makes me so excited \
all the time because I love to {verb1}. Stay hydrated and {verb2} \
like you are {famous_person}"

print(madlib)

# # METHOD 2 

madlib = "Computer Programming is so " + adj + "! "+ "It makes me so excited all the time \
because I love to " + verb1 + ". " + "Stay hydrated and "+ verb2  + "like \
you are "+ famous_person

print(madlib)

# METHOD 3

madlib = "Computer Programming is so {}! It makes me so excited all the \
time because I love to {}. Stay hydrated and {} like you are {}".format(adj,verb1,verb2,famous_person)

print(madlib)