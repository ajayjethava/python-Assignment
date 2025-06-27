""" Write a Python program to show multiple inheritance. """


class Father:
    def skills_father(self):
        print("Father's skills")

class Mother:
    def skills_mother(self):
        print("Mother's skills")

class Child(Father, Mother):
    def skills_child(self):
        print("Child's skills")


child = Child()
child.skills_father()
child.skills_mother()
child.skills_child()


print()
print("next ...")
print()