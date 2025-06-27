"""Write a Python program to search for a word in a string usingre.search(). """


import re

text = "Welcome to Python programming."
word = "Python"

match = re.search(word, text)

if match:
    print(f"'{word}' found in the string.")
else:
    print(f"'{word}' NOT found in the string.")


print()
print("next ...")
print()


