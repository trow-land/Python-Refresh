# Lists - A Data Structure

li = [1, 2, 3, 4, 5]  # Inside the square brackets we can have different objects

li2 = ['a', 'b', 'c']  # In python lists are a form of array - a collection of items

li3 = [1, 2.0, "d", True]  # They can contain multiple types

print(li3)  # [1, 2.0, 'd', True]


# List slicing

shopping_list = [
    "Apples",
    "Pasta",
    "Tomatoes",
    "Potatoes",
    "Salmon"]

print(shopping_list)  # ['Apples', 'Pasta', 'tomatoes', 'potatoes', 'salmon']

# You can iterate over lists like strings
print(shopping_list[::-1])  # ['salmon', 'potatoes', 'tomatoes', 'Pasta', 'Apples']

# Lists are mutable, which means you can change individual elements.
shopping_list[1] = "Spaghetti Pasta"
print(shopping_list)  # ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon']

print(len(shopping_list))  # 5
shopping_list.append("Hummus")
print(len(shopping_list))  # 6
print(shopping_list)  # ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus']

# Here we're not creating a new list, but creating a new reference or pointer to the same list.
new_shopping_list = shopping_list  # Points to location in memory
newest_shopping_list = shopping_list[:]  # Creates a copy

# When we modify new_shopping_list, it also changes shopping_list.
# This is because both new_shopping_list and shopping_list are referencing the same underlying list in memory.
new_shopping_list[0] = "Bananas"

print("Original: ", shopping_list)  # ['Bananas', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus']
print("New: ", new_shopping_list)  # ['Bananas', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus']


# To make a copy  of a list you need to slice the list
# newest_shopping_list = shopping_list[:]
print("Newest: ", newest_shopping_list)  # ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus']


# List Methods
new_item = "Chocolate"
newest_shopping_list.append(new_item)
print(newest_shopping_list)  # ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus', 'Chocolate']
# Append changes the list inplace

# newest_shopping_list.append(input("Item to add: "))
# print(newest_shopping_list)

new_items = ["Toothpaste", "Carrots"]
newest_shopping_list.extend(new_items)  # The extend method adds each element of the iterable to the list
print(newest_shopping_list) #  ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus', 'Chocolate', 'milkshake', 'toothpaste', 'carrots']

newest_shopping_list.pop()  # Removes the last item in the list
print(newest_shopping_list)  # ['Apples', 'Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus', 'Chocolate', 'milkshake', 'toothpaste']


newest_shopping_list.pop(0)  # Removes the item at index 0
print(newest_shopping_list)  # ['Spaghetti Pasta', 'tomatoes', 'potatoes', 'salmon', 'Hummus', 'Chocolate', 'milkshake', 'toothpaste']


newest_shopping_list.remove("Tomatoes")  # The Remove method removes a specific item
print(newest_shopping_list)  # ['Spaghetti Pasta', 'potatoes', 'salmon', 'Hummus', 'Chocolate', 'milkshake', 'toothpaste']

newest_shopping_list.clear()  # Removes everything from the list
print(newest_shopping_list)  # []

newest_shopping_list = shopping_list[:]
print(newest_shopping_list.index("Salmon"))  # 4, returns the index of the item in question

print("Broccoli" in newest_shopping_list)  # False,  Returns if the item is in the list

# Create a sorted copy of the list
sorted_list = sorted(newest_shopping_list)  # ['Bananas', 'Hummus', 'Potatoes', 'Salmon', 'Spaghetti Pasta', 'Tomatoes']
print(sorted_list)  # Prints the sorted copy of the list

# Sort the list in-place
newest_shopping_list.sort()  # ['Bananas', 'Hummus', 'Potatoes', 'Salmon', 'Spaghetti Pasta', 'Tomatoes']
print(newest_shopping_list)  # Prints the list sorted in-place

newest_shopping_list.reverse()
print(newest_shopping_list)  # ['Tomatoes', 'Spaghetti Pasta', 'Salmon', 'Potatoes', 'Hummus', 'Bananas']



# Common list patterns
print(len(newest_shopping_list))  # 6
print(list(range(1,5)))  # [1, 2, 3, 4]
print(list(range(5)))  # [0, 1, 2, 3, 4]

sentence = ""
new_sentence = sentence.join(["I am refreshing my python skills"])
print(new_sentence)


# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(other)  # [4, 5, 6, 7]
print(d)  # 8
