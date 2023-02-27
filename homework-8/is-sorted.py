def is_sorted(lst, reverse=False):
    n = len(lst)
    if n <= 1:
        return True
    if not reverse:
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                return False
    else:
        for i in range(n - 1):
            if lst[i] < lst[i + 1]:
                return False
    return True


ls = [2, 3, 4]

print(is_sorted(ls))