#   Write a generator function that generates the first 10 even numbers.




def range():
    num = 0
    while num < 10:
        yield num
        num += 2

for i in range():
    print("even number is :",i)

    
    
    

