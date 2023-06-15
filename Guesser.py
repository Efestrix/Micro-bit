import random
tajne_cislo = random.randint (0, 100)
while True:
    guess = int(input ("write number:"))
    if tajne_cislo == guess:
        print("let's goo")
    elif guess > tajne_cislo:
        print("lower")
    elif guess < tajne_cislo:
        print("higher")
