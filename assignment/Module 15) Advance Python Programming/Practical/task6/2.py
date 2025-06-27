"""Write a Python program to demonstrate the use of local and
global variables in a class."""




manufacturer = "Global Motors"

class Bike:
    def __init__(self, model):
        self.model = model  

    def show_info(self):
    
        year = 2023
        print(f"Manufacturer: {manufacturer}")  
        print(f"Model: {self.model}")            
        print(f"Year: {year}")                    

bike1 = Bike("Harley")
bike1.show_info()