num = int(input("Enter a number: "))
f_num = 0
s_num = 1
fib_num = f_num + s_num

if num <= 0:
    fib_num = "Incorrect input"
elif num == 1:
    fib_num = f_num
elif num == 2:
    fib_num = s_num

list_of_fib_nums = []
for i in range(3, num + 1):
    fib_num = f_num + s_num
    f_num = s_num
    s_num = fib_num
    list_of_fib_nums.append(fib_num)

print(list_of_fib_nums)