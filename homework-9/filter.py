def my_filter(function, iterable):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    yield result



x = [1, 2, 3]
filtered_x = my_filter(lambda y: y > 1, x)
print(filtered_x)