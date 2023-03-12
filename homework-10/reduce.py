def my_reduce(function, iterable, initializer=None):
    while len(iterable)>= 2:
        i = 0
        initializer = function(iterable[i], iterable[i+1])
        iterable.insert(i+2, initializer)
        iterable = iterable[2:]
    return initializer

lis = [1, 3, 5, 6, 2]
r = my_reduce(lambda a, b: a if a > b else b, lis)
print(r)