import random
import string

a = (''.join(random.choice(string.ascii_letters) for i in range(10)))
print("Сгенерированое значение:", a)
b = a.lower()

print(f'{b[0].title()}({b[0]}) выводится', b.count(b[0]), "раз(а)")
print(f"{b[1].title()}({b[1]}) выводится", b.count(b[1]), "раз(а)")
print(f"{b[2].title()}({b[2]}) выводится", b.count(b[2]), "раз(а)")
print(f"{b[3].title()}({b[3]}) выводится", b.count(b[3]), "раз(а)")
print(f"{b[4].title()}({b[4]}) выводится", b.count(b[4]), "раз(а)")
print(f"{b[5].title()}({b[5]}) выводится", b.count(b[5]), "раз(а)")
print(f"{b[6].title()}({b[6]}) выводится", b.count(b[6]), "раз(а)")
print(f"{b[7].title()}({b[7]}) выводится", b.count(b[7]), "раз(а)")
print(f"{b[8].title()}({b[8]}) выводится", b.count(b[8]), "раз(а)")
print(f"{b[9].title()}({b[9]}) выводится", b.count(b[9]), "раз(а)")
