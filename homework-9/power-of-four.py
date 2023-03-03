num = int(input())

p_num = num

while p_num % 4 == 0:
    p_num = p_num / 4

if p_num == 1:
    print(f'{num} is a power of four')
else:
    print(f'{num} is not a power of four')