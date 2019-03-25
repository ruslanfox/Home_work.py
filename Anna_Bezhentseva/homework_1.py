import random

a = random.randint(1000, 1000000)
print("Generated number ", a)
b = a // 1000 % 10
print("The fourth digit ", b)
