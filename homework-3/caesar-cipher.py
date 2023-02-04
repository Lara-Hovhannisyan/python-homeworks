plain = input()
shift = int(input())
plain_list = list(plain)
encrypted = []

for i in plain_list:
    if i.islower():
        encrypt = chr((ord(i) - shift - 97) % 26 + 97)
        encrypted.append(encrypt)
    elif i.isupper():
        encrypt = chr((ord(i) - shift - 65) % 26 + 65)
        encrypted.append(encrypt)
    else:
        encrypted.append(i)


print(''.join(encrypted))

