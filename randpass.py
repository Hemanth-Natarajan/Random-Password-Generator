import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("Your password is :")
#Random password but in sequence [letters+symbols+numbers]
ulet = []
for i in letters[0:nr_letters]:
    ulet.append(random.choice(letters))
for j in symbols[0:nr_symbols]:
    ulet.append(random.choice(symbols))
for k in numbers[0:nr_numbers]:
    ulet.append(random.choice(numbers))
print(''.join(ulet))

#Random Password without using shuffle function
total_len = len(ulet)
randpass = []
for i in range(0,total_len):
    randpass.append(random.choice(ulet))

print(''.join(randpass))

#Random password using random.shuffle function

random.shuffle(ulet)
print(''.join(ulet))