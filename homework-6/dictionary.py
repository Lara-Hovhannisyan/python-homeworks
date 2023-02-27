file = open("dictionary.txt", "r", encoding="utf8")
dictionary = {}
for line in file:
    k, v = line.split(' - ')
    dictionary[k] = v.strip()
file.close()
print(dictionary)
