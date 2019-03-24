import string
import random
res = random.sample(string.ascii_letters, 10)
print(''.join(res))
for letter in res:
    print(f"Letter \"{letter}\" is repeat {res.count(letter)} times")
