word = input()
palindrome = True
last_char = len(word) - 1

for i in range(len(word)//2):
    if word[i] != word[last_char]:
        palindrome = False
        break
    last_char -= 1

if palindrome:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")

