size = int(input("Enter matrix size: "))

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
input_list = input("matrix = ")
lst = [int(item) for item in input_list.replace("[", "").replace("]", "").split(', ')]
matrix = [lst[i:i+size] for i in range(0, len(lst), size)]

transposed = [list(row) for row in zip(*matrix)]
# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print(f'transpose = {transposed}')