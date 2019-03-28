import random
import string

ourLetters = string.ascii_letters
print(ourLetters)
ourRandomLetters = random.sample(ourLetters, 10)
print(ourRandomLetters)
ourCheckString = "".join(ourRandomLetters).lower()
print(ourCheckString)
print(ourCheckString.count(ourCheckString[0]))
print(ourCheckString.count(ourCheckString[1]))
print(ourCheckString.count(ourCheckString[2]))
print(ourCheckString.count(ourCheckString[3]))
print(ourCheckString.count(ourCheckString[4]))
print(ourCheckString.count(ourCheckString[5]))
print(ourCheckString.count(ourCheckString[6]))
print(ourCheckString.count(ourCheckString[7]))
print(ourCheckString.count(ourCheckString[8]))
print(ourCheckString.count(ourCheckString[9]))
