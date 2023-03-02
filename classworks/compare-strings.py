str1 = input()
str2 = input()

for i in str1:
    if str1 == str2:
        print('0')
        break
    elif len(str1) != len(str2):
        print(-1)
        break
    elif len(str1) == len(str2) and i not in str2:
        print(i)
