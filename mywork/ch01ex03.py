#!/usr/bin/env python3

input_string = input("Enter a string: ")

input_string.endswith('.') and print("Ends with a period.")
input_string.isalpha() and print("All characters are alphabetic.")
input_string.find('x') != -1 and print("Contains the letter 'x'.")

print(input_string.replace('e', 'E'))


