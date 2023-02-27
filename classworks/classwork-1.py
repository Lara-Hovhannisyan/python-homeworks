# Cat
# string = input()
# ls = []
# for i in range(len(string)):
#     word = string[:i] + string[i].capitalize() + string[i+1:]
#     ls.append(word)
# print(ls)

# Compare strings
# str1 = input()
# str2 = input()
#
# for i in str1:
#     if str1 == str2:
#         print('0')
#         break
#     elif len(str1) != len(str2):
#         print(-1)
#         break
#     elif len(str1) == len(str2) and i not in str2:
#         print(i)
#


# String in string
# def str_in_str(str1, str2):
#     for i in str2:
#         if i in str1:
#             return str1.index(i)
#
#
# print(str_in_str('HelloWorld', 'World'))

# string = “Hello”, number = 2, bool = True, Output: loHel

# Move string
# def str_move(string, number, boolean):
#     if boolean:
#         string = string[-number:] + string[:-number]
#     else:
#         string = string[number:] + string[:number]
#     return string
#
#
# print(str_move("Hello", 2, False))

# Numbers's index
# def nums_index(ls, target):
#     if target in ls:
#         return ls.index(target)
#     else:
#         for i in range(len(ls) - 1):
#             if ls[i] < target < ls[i + 1]:
#                 ls.append(target)
#                 ls.sort()
#                 return ls.index(target)
#
#
# print(nums_index([1, 3, 5, 6, 7, 9], 10))

# Create Matrix
# a, b = int(input()), int(input())
# def create_matrix(m, n):
#     return [[i * j for j in range(n)] for i in range(m)]
#
#
# print(create_matrix(a, b))

# Check password
# test_str = input("Enter a password: ")
# res = False
# if 6 <= len(test_str) <= 16:
#     for ele in test_str:
#         if ele.isupper() and ele.isdigit():
#             res = True
#             break
#         if '$' in test_str or '#' in test_str or '@' in test_str:
#             res = True
#             break
#     if res:
#         print("Valid password")
#     else:
#         print("Not valid password")
# else:
#     print("Not valid password")