number = int(input('Enter a number: '))

bnum = bin(number)
seq_bnum = list(bnum)
sum_ = 0
for i in range(len(seq_bnum)):
    if seq_bnum[i] == '1':
        sum_ += 1
print(sum_)