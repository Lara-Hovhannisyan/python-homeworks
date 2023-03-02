def str_move(string, number, boolean):
    if boolean:
        string = string[-number:] + string[:-number]
    else:
        string = string[number:] + string[:number]
    return string


print(str_move("Hello", 2, False))