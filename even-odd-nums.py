"""Write a program that asks the user to enter a number, checks, 
and prints whether the number is even or odd.
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")
