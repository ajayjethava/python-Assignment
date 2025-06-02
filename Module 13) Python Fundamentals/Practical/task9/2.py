#  Write a Python program that manipulates and prints strings using various string methods.



text = "  Hello, Python World! Welcome to Python Programming.  "


stripped_text = text.strip()
print("Stripped:", stripped_text)

upper_text = stripped_text.upper()
print("Uppercase:", upper_text)

lower_text = upper_text.lower()
print("Lowercase:", lower_text)

capitalized_text = lower_text.capitalize()
print("Capitalized:", capitalized_text)

title_text = capitalized_text.title()
print("Title Case:", title_text)

swapped_text = title_text.swapcase()
print("Swapped Case:", swapped_text)

replaced_text = swapped_text.replace("Python", "Java")
print("Replaced 'Python' with 'Java':", replaced_text)

count_python = replaced_text.count("Java")
print("Occurrences of 'Java':", count_python)

index_python = replaced_text.find("Java")
print("Index of 'Java':", index_python)

split_text = replaced_text.split()
print("Split into words:", split_text)

joined_text = " ".join(split_text)
print("Joined back into a string:", joined_text)

starts_with_hello = replaced_text.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

ends_with_programming = replaced_text.endswith("Programming.")
print("Ends with 'Programming.':", ends_with_programming)

is_alphanumeric = replaced_text.isalnum()
print("Is alphanumeric:", is_alphanumeric)

is_alpha = replaced_text.isalpha()
print("Is alphabetic:", is_alpha)

is_digit = replaced_text.isdigit()
print("Is digit:", is_digit)
