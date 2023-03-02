def nums_index(ls, target):
    if target in ls:
        return ls.index(target)
    else:
        for i in range(len(ls) - 1):
            if ls[i] < target < ls[i + 1] or target < ls[0] or target > ls[-1]:
                ls.append(target)
                ls.sort()
                return ls.index(target)


print(nums_index([2, 3, 5, 6, 7, 9], 10))