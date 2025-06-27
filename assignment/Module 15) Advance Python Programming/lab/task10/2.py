"""Write a Python program to match a word in a string using re.match()."""





import re

text = "Python is a powerful language."


word = "Python"

match = re.match(word, text)

if match:
    print(f"The string starts with the word '{word}'.")
else:
    print(f"The string does NOT start with the word '{word}'.")