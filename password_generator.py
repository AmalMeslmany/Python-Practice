import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*?"

all_characters = letters

length = int(input("Enter password length: "))

include_numbers = input("Include numbers? (y/n): ")
include_symbols = input("Include symbols? (y/n): ")

if include_numbers.lower() == "y":
    all_characters += numbers

if include_symbols.lower() == "y":
    all_characters += symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:", password)