word = input()

if len(word) == 1:
    palindrome = True
else:
    palindrome = False
    last_char = len(word) - 1
    for i in range(len(word)//2):
        if word[i] == word[last_char]:
            palindrome = True
            last_char -= 1
        else:
            palindrome = False

if palindrome:
    print(f"The {word} word is palindrome")
else:
    print(f"The {word} word is not palindrome")

