#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
p1 = []
if nr_letters < 2 or nr_symbols < 2 or nr_numbers < 2:
    print("You must have at least 2 letter, 2 number and 2 symbols in your password")
elif nr_letters > len(letters):
    print(f"You can only have {len(letters)} letters in your password")
else:
    for i in range(0, nr_letters):
        r = random.randint(0, len(letters) - 1)
        p1.append(letters[r])

    for i in range(0, nr_symbols):
        s = random.randint(0, len(symbols) - 1)
        p1.append(symbols[s])

    for i in range(0, nr_numbers):
        n = random.randint(0, len(numbers) - 1)
        p1.append(numbers[n])

    random.shuffle(p1)
    listasstring = ''.join(p1)
    print(listasstring)
