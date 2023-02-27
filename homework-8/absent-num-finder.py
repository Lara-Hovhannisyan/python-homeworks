def absent_num(lst):
    max_num = max(lst)
    absent_numbers = []
    for i in range(1, max_num + 1):
        if i not in lst:
            absent_numbers.append(i)
    if absent_numbers:
        return absent_numbers
    else:
        return None


# ls = [1, 2, 3, 4, 5, 6, 8, 9]
# print(absent_num(ls))
