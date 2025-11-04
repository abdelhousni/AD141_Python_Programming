#!/usr/bin/env python3

input_sentence = input("Enter a sentence: ")

occurences_of_first = input_sentence.lower().count(input_sentence[0].lower())
occurences_of_last = input_sentence.lower().count(input_sentence[-1].lower())


print(f"The first character '{input_sentence[0]}' appears {occurences_of_first} times in the sentence.\n")
print(f"The last character '{input_sentence[-1]}' appears {occurences_of_last} times in the sentence.\n")

