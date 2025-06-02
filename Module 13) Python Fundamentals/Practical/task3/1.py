#   Write a Python program to demonstrate the creation of variables and different data types.



# Numeric Data Types
integer_var = 42
float_var = 3.14
complex_var = 2 + 3j

# String Data Type
string_var = "Hello, Python!"

# Boolean Data Type
bool_var = True

# Sequence Data Types
list_var = [1, 2, 3, 4, 5]
tuple_var = (10, 20, 30)
range_var = range(5)

# Mapping Data Type
dict_var = {"name": "Alice", "age": 30}

# Set Data Types
set_var = {1, 2, 3}
frozenset_var = frozenset([4, 5, 6])

# Binary Data Types
bytes_var = b"Hello"
bytearray_var = bytearray([65, 66, 67])

# None Data Type
none_var = None

# Displaying the values and their types
print(f"integer_var = ",integer_var, "Type:",type(integer_var))
print(f"float_var = ",float_var, "Type: ",type(float_var))
print(f"complex_var = ",complex_var, "Type: ",type(complex_var))
print(f"string_var = ",string_var, "Type: ",type(string_var))
print(f"bool_var = ",bool_var, "Type: ",type(bool_var))
print(f"list_var = ",list_var, "Type: ",type(list_var))
print(f"tuple_var = ",tuple_var, "Type: ",type(tuple_var))
print(f"range_var = ",list(range_var), "Type: ",type(range_var))
print(f"dict_var = ",dict_var, "Type: ",type(dict_var))
print(f"set_var = ",set_var, "Type: ",type(set_var))
print(f"frozenset_var = ",frozenset_var, "Type: ",type(frozenset_var))
print(f"bytes_var = ",bytes_var, "Type: ",type(bytes_var))
print(f"bytearray_var = ",bytearray_var, "Type: ",type(bytearray_var))
print(f"none_var = ",none_var, "Type: ",type(none_var))

