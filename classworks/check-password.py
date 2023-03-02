test_str = input("Enter a password: ")
res = False
if 6 <= len(test_str) <= 16:
    for ele in test_str:
        if ele.isupper() and ele.isdigit():
            res = True
            break
        if '$' in test_str or '#' in test_str or '@' in test_str:
            res = True
            break
    if res:
        print("Valid password")
    else:
        print("Not valid password")
else:
    print("Not valid password")