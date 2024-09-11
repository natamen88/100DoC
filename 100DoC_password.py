import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#number of letters is 52
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#number of numbers is 10
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#number of symbols is 9

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#random letters generation
list_letters = []
password_letters = []
for number in range(0, nr_letters):
    list_letters.append(random.randint(0,51))
    password_letters.append(letters[list_letters[number]])

#random numbers generation
list_numbers = []
password_numbers = []
for number in range(0, nr_numbers):
    list_numbers.append(random.randint(0,9))
    password_numbers.append(numbers[list_numbers[number]])

#random symbols generation
list_symbols = []
password_symbols = []
for number in range(0, nr_symbols):
    list_symbols.append(random.randint(0,8))
    password_symbols.append(symbols[list_symbols[number]])

final_password = (password_letters+password_symbols+password_numbers)
print(final_password)
password = "".join(final_password)
print("Password is: " + password)

random.shuffle(final_password)
password2 = "".join(final_password)
print("Password is: " + password2)