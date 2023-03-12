def my_filter(function, iterable):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    yield result



x = [1, 2, 3]
filtered_x = my_filter(lambda y: y > 1, x)
print(filtered_x)


# def my_filter(func, iterable):
#     res = []
#     if func is None:
#         for i in iterable:
#             if i:
#                 res.append(i)
#         yield res
#     for i in iterable:
#         if func(i):
#             res.append(i)
#     yield res
