size = int(input("Enter matrix size: "))

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = input("matrix = ")
lst1 = lst.replace("[", "").replace("]", "")
lst2 = [int(item) for item in lst1.split(', ')]
nested_lst = [lst2[i:i+size] for i in range(0, len(lst2), size)]


transposed = [[row[i] for row in nested_lst] for i in range(len(nested_lst[0]))]


print(f'transpose = {transposed}')