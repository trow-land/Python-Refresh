# Built-in functions and methods

number = "123456789"
print(len(number))  # 9, len() is a built-in function that returns the length (number of items) of an object.

# len counts like a human from 1

# A built-in function has the syntax name()

# Python methods are similar but are owned by something such as a string or list

# For example, lower() is a string method that converts all uppercase characters in a string into lowercase characters
text = "HELLO, WORLD!"
text = text.lower()
print(text)  # "hello, world!"

text = text.capitalize()
print(text)  # Hello, world!

text = text.upper()
print(text)  # "HELLO, WORLD!"

print(text.find("!"))  # 12, Finds the index at which a ! is found

text2 = text.replace("WORLD", "UNIVERSE")
print(text2)

# Python methods have the syntax object.method()

# Another built-in function: sum(). This function returns the sum of all items in an iterable (like a list or tuple).
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15


# Here's another string method: split(). This splits a string into a list where each word is a list item.
sentence = "This is a test."
print(sentence.split())  # ["This", "is", "a", "test."]
