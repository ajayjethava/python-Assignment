"""Write Python programs to demonstrate method overloading and method overriding"""




class MathOperations:
    def add(self, a, b, c=0):
    
        return a + b + c

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


math = MathOperations()

print(math.add(2, 3))        
print(math.add(2, 3, 4))     
print(math.multiply(2, 3))   
print(math.multiply(2, 3, 4))


print()
print("next ...")
print()

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  
        print("Dog barks")

animal = Animal()
animal.speak()  

dog = Dog()
dog.speak()     