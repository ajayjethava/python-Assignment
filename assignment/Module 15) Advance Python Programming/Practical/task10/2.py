""" Write a Python program to match a word in a string using re.match()."""





import re

text = "Python is awesome."
word = "Python"

match = re.match(word, text)

if match:
    print(f"The string starts with '{word}'.")
else:
    print(f"The string does NOT start with '{word}'.")