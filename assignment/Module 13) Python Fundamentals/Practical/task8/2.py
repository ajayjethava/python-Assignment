#  Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
#  the break statement.




m = ['apple', 'banana', 'cherry', 'date']

for i in m:
    print("Checking: ",i)
    if i == 'banana':
        print("Found 'banana'! Stopping the loop.")
        break
else:
    print("'banana' was not found in the list.")

