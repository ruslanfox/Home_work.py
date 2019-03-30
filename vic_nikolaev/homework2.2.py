import string
import random

# 1 version
letters = string.ascii_letters
one = random.choice(letters)
two = random.choice(letters)
three = random.choice(letters)
four = random.choice(letters)
five = random.choice(letters)
six = random.choice(letters)
seven = random.choice(letters)
eight = random.choice(letters)
nine = random.choice(letters)
ten = random.choice(letters)

word = f"{one}{two}{three}{four}{five}{six}{seven}{eight}{nine}{ten}"
print(word)

print(f"Буква {one} - {word.count(one)}")
print(f"Буква {two} - {word.count(two)}")
print(f"Буква {three} - {word.count(three)}")
print(f"Буква {four} - {word.count(four)}")
print(f"Буква {five} - {word.count(five)}")
print(f"Буква {six} - {word.count(six)}")
print(f"Буква {seven} - {word.count(seven)}")
print(f"Буква {eight} - {word.count(eight)}")
print(f"Буква {nine} - {word.count(nine)}")
print(f"Буква {ten} - {word.count(ten)}")

# 2 version
word2 = (''.join(random.sample(string.ascii_letters, 10)))
print(word2)

word2 = word2.lower()

print(f"{word2[0]} - {word2.count(word2[0])}")
print(f"{word2[1]} - {word2.count(word2[1])}")
print(f"{word2[2]} - {word2.count(word2[2])}")
print(f"{word2[3]} - {word2.count(word2[3])}")
print(f"{word2[4]} - {word2.count(word2[4])}")
print(f"{word2[5]} - {word2.count(word2[5])}")
print(f"{word2[6]} - {word2.count(word2[6])}")
print(f"{word2[7]} - {word2.count(word2[7])}")
print(f"{word2[8]} - {word2.count(word2[8])}")
print(f"{word2[9]} - {word2.count(word2[9])}")
