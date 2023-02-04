phone_num = input()
numbers = list(phone_num)
length = len(numbers)

if (length != 12) and (length != 14):
    print("Invalid")
    exit()

count = 0
for i in range(length):
    if i == length-1 and numbers[i].isdigit():
        continue
    elif i == 0 and numbers[i] == '1' and numbers[i+1] == '-':
        count = 3
    elif numbers[i].isdigit():
        count += 1
    elif count == 3 and numbers[i] == '-':
        count = 0
    else:
        print("Invalid")
        exit()
print("Valid")

