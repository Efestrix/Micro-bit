my_input = "ahoj"
alphabet="abcdefghijklmnopqrstuvwxyz"

for char in my_input:
    original_index= alphabet.index(char)
    new_index = original_index - 3
    print(alphabet[original_index] + " - " +alphabet[new_index])
