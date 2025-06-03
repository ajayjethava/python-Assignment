#  Create a mini-project where students combine conditional statements, loops, and functions
#  to create a basic Python application, such as a simple calculator or a grade management
#  system.



while True:
    menu="""
Select operation:
press 1 for Add
press 2 for Subtract
press 3 for Multiply
press 4 for Divide
press 5 for exit 
    """


    print(menu)
    choice = input("Enter choice : ")

    if choice in ('1', '2', '3', '4',):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1 ,"+", num2, "=", num1 + num2)
            
        elif choice == '2':
            print(num1, "-" ,num2, "=" ,num1 - num2)
            
        elif choice == '3':
            print(num1, "*", num2, "=" ,num1 * num2)
            
        elif choice == '4':
            if num2 != 0:
                print(num1, "/", num2 ,"=", num1 / num2)
            else:
                print("Error! Division by zero.")
                
    elif choice=='5':
            print("THanks you")
            break
    else:
        print("Invalid Input")
        break
    
