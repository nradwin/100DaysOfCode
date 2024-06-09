# import random for element selection and shuffling
import random

# lists of possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# dialogue and input for password
print("Radwin Password Manager\nLet's create a new, secure password for you:")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# init list
password = []

# add random selection letters, symbols, and numbers, as many as the user wants for each
for letter in range(nr_letters):
  password += random.choice(letters) 

for symbol in range(nr_symbols):
  password += random.choice(symbols)

for number in range(nr_numbers):
  password += random.choice(numbers)

# randomly shuffle list
random.shuffle(password)

# convert list to string
password = ''.join(password)

# print randomized, secure password
print(password)