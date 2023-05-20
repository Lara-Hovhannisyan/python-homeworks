class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def square(num):
        return num ** 2


a = 5
b = 10

result_add = Math.add(a, b)
print(f"{a} + {b} = {result_add}")

result_multiply = Math.multiply(a, b)
print(f"{a} * {b} = {result_multiply}")

num = 7
result_square = Math.square(num)
print(f"The square of {num} is {result_square}")
