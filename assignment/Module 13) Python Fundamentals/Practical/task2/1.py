#  Write a Python program that demonstrates the correct use of indentation, comments, and
#   variables following PEP 8 guidelines.




def fun(name: str) -> str:
  
    name = name.capitalize()
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = "ajay" 
    a= fun(user_name)
    print(a)

