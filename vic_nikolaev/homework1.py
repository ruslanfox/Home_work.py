import random

num = random.randint(1000, 1000000)
print(num)

num %= 10000
num //= 1000
print(num)
