string = input()
ls = []
for i in range(len(string)):
    word = string[:i] + string[i].capitalize() + string[i+1:]
    ls.append(word)
print(ls)