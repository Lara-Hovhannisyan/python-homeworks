def str_in_str(str1, str2):
    for i in str2:
        if i in str1:
            return str1.index(str2)


print(str_in_str("HeWlloWorld", "World"))

# string = “Hello”, number = 2, bool = True, Output: loHel