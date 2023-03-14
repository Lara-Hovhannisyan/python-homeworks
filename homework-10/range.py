def my_range(start=0, stop=None, step=1):
    res = []
    if stop is None:
        stop = start
        start = 0
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        res.append(start)
        start += step
    return res

ls = [1,2,3,4,5]
# x = my_range(10, 6, -2)
for n in my_range(len(ls)):
  print(n)

