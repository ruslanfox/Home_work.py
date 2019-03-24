# This is regular strings
print('Just a regular string')
print("Just a regular string")

# docstring support newlines
print("""Doc string with newlines
      perfectly work""")
print('''Doc string with newlines
      perfectly work''')

# there is a feature with strings, that allows to split them across lines
# although keeping them as a single line for python
print(
    'test'
    ' this is still the same line '
    'even if it looks splitted'
)

# cool operation with strings
print("You" + " can" + " add string like this")  # Concatenate them
print("Multiplication!" * 3)  # Multiply them
# format them
a = "Bond"
print("My name is %(name)s, James %(name)s" % {"name": a})
print("My name is {name}, James {name}".format(name=a))
print(f"My name is {a}, James {a}")  # python >= 3.6

# some usefull functions
print("Split, This, by, comma_space".split(", "))
print(" ".join(["Join", "This", "With", "Space"]))
