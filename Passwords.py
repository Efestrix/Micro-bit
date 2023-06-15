import string
import random

password = ""
delka = int(input("Napis cislo:"))
pocet_hesel = int(input("pocet hesel:"))
chars = string.punctuation + string.ascii_letters + string.digits
len(chars)

for j in range(pocet_hesel):
    password = ""
    for i in range(delka):
        password = password + random.choice(chars)
    print(password)
