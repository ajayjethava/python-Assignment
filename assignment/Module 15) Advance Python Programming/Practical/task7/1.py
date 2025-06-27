"""Write a Python program to show single inheritance."""


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

child = Child()
child.greet()        
child.greet_child()  


print()
print("next ...")
print()