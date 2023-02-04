lst = [item for item in input().split()]
new_lst = []
for i in range(len(lst)):
    if i != len(lst) - 1:
        lst[i] += '+'
    new_lst.append(lst[i])
string = ''.join(lst)
print(string)