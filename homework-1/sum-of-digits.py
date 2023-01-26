"""Write a program that asks the user to enter a number and prints the sum of its digits on the screen."""

num = int(input("Enter a number: "))

sum_ = 0
while num != 0:
    sum_ = sum_ + num % 10
    num = num // 10
print(sum_)
