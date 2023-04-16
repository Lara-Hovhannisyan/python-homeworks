def my_filter(func, iterable):
    res = []
    for i in iterable:
        if func is None:
            if i:
                res.append(i)
        elif func(i):
            res.append(i)
    return res

x = [1, 2, 3, 0]
# filtered_x = my_filter(lambda y: y > 1, x)
filtered_x = my_filter(None, x)
print(filtered_x)