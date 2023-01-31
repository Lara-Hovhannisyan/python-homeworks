lst = [int(item) for item in input("Enter the list items : ").split()]

max_num = 0
num = 0
for i in range(len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]
print(max_num)

