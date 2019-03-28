textField = input("Enter some text: ")
wordField = input("Enter the word for checking: ")
result = textField.lower().count(wordField.lower())
print(f"Word \"{wordField}\" is met in the given text {result} times")
