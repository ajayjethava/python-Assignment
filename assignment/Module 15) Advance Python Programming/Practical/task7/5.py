"""Write a Python program to show hybrid inheritance."""






class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")


obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()



print()
print("next ...")
print()
