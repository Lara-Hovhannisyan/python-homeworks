"""Write a program that asks the user to enter a character, checks,
and prints whether the character is a consonant or a vowel."""

char = ""

while not char.isalpha():
    char = input("Enter a character: ")

if char in ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]:
    print("It's a vowel character.")
else:
    print("It's a consonant character.")
