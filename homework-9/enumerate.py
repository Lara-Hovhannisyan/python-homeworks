def enum(iterable, start=0):
    if start > len(iterable):
        return
    count = start
    for el in iterable:
        yield count, el


