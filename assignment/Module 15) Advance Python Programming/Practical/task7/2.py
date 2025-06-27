"""Write a Python program to show multilevel inheritance."""


class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")


c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()

print()
print("next ...")
print()