a = input("Введите текст:  ").lower()
b = input("Введите слово: ").lower()
print(f"Слово", b.title(), "встреается в тексте", a.count(b), "раз(а)")
