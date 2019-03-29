import random
import string

gener = string.ascii_lowercase
w = random.choices(gener, k=10)
word = ' '.join(map(str, (w)))

print(word)

print("Перша літера зустрічається", w.count(w[0]), "раз(и)")
print("Друга літера зустрічається", w.count(w[1]), "раз(и)")
print("Третя літера зустрічається", w.count(w[2]), "раз(и)")
print("Четверта літера зустрічається", w.count(w[3]), "раз(и)")
print("Пʼята літера зустрічається", w.count(w[4]), "раз(и)")
print("Шоста літера зустрічається", w.count(w[5]), "раз(и)")
print("Сьома літера зустрічається", w.count(w[6]), "раз(и)")
print("Восьма літера зустрічається", w.count(w[7]), "раз(и)")
print("Девʼята літера зустрічається", w.count(w[8]), "раз(и)")
print("Десята літера зустрічається", w.count(w[9]), "раз(и)")
