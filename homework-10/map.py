def my_map(function, iterable):
    for i in iterable:
        yield function(i)


ls = [2,3]

print(list(map(lambda x: x+1, ls)))