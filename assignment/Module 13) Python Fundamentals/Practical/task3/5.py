#  Practical Example 4: How to check the type of a variable dynamically using type().





def fun(variable):
    var_type = type(variable)
    print(f"The variable has type: ",var_type)

fun(42)            # Integer
fun("Hello")       # String
fun([1, 2, 3])     # List
fun(3.14)          # Float
fun(True)          # Boolean
