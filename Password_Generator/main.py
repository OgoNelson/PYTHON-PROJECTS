import random

letters = ["a", "b", "c", "d", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "%", "^", "&", "*", "(", ")"]

#getting password length and distribution from the user
print("Welcome to Password Generator")
num_letters = int(input("How many letters do you need in the password?\n"))
num_numbers = int(input("How many numbers do you need in the password?\n"))
num_symbols = int(input("How many symbols do you need in the password?\n"))

#selecting password components randomly
password_list = []
for chars in range(1, num_letters + 1):
    password_list += random.choice(letters)

for chars in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

for chars in range(1, num_symbols + 1):
    password_list += random.choice(symbols)

#rearranging the password_list chars
random.shuffle(password_list)

#converting the password to a string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")