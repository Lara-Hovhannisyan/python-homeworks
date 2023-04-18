string = input()
unique = ""
for char in string:
    if char not in unique:
        unique += char
print(unique)