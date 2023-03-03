ages = [5, 12, 15, 17, 18, 24, 32]


def teen_ages(age):
    if 13 < age < 20:
        return True
    else:
        return False


teens = filter(teen_ages, ages)

for x in teens:
    print(x)