a, b = int(input()), int(input())


def create_matrix(m, n):
    return [[i * j for j in range(n)] for i in range(m)]


print(create_matrix(a, b))