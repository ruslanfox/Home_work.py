text = input()
word = input()

result = text.lower().count(word.lower())
print(f"Слово {word} встречается в этом предложении {result} раз")
