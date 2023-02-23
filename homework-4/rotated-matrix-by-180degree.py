size = int(input("Enter matrix size: "))

lst = []


for i in range(size):
    single_row = list(map(int, input().split()))
    lst.append(single_row)

rev = [i[::-1] for i in lst]

rev.reverse()

for i in range(len(rev)):
    for j in range(len(rev[0])):
        print(rev[i][j], end=' ')
    print()

