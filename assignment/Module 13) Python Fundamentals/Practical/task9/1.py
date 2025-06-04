#  Write a Python program to demonstrate string slicing.




m = "Hello, Python World!"

print("Basic slicing:")
print("First 5 characters:", m[:5])  
print("Characters from index 7 to 12:", m[7:13])  


print("\nUsing negative indices:")
print("Last 6 characters:", m[-6:]) 
print("Characters from index -13 to -7:", m[-13:-7]) 

print("\nSlicing with step:")
print("Every second character:", m[::2])  

print("\nSlicing with step and negative indices:")
print("Every second character from the end:", m[::-2])  
