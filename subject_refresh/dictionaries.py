# A dictionary in Python is a mutable, unordered collection of unique key-value pairs.

#
# Lists: Use Lists when you want a collection of items where order matters and items can be changed. Lists are great for
# keeping track of things by order, especially when the order and contents might change.
#
# Linked Lists: Use Linked Lists when you need to insert or delete elements at both ends efficiently. They are great for
# creating other data structures like stacks and queues.
#
# Tuples: Use Tuples when you have a collection of items that are ordered and immutable. They're often used for groups
# of related data that won't change, such as the coordinates of a point in space.
#
# Sets: Use Sets when you need to store a collection of unique items where order doesn't matter. They're useful for
# eliminating duplicate entries and checking membership efficiently.
#
# Dictionaries: Use Dictionaries when you need a set of unique keys mapping to values. They are great for fast lookups,
# as you can access any value by its key.
#
# Strings: Use Strings to handle textual data. They're basically lists of characters, allowing you to do things like
# indexing and slicing.
#
# Queues: Use Queues when you want to handle items in a first-in-first-out manner. They're great for scheduling
# operations in many types of algorithms.
#
# Stacks: Use Stacks when you need last-in-first-out behavior. They're useful in algorithms where you need to backtrack,
# like navigating a maze.
#
# Heapq (Heap Queue): Use Heaps when you want to always access the highest or lowest element. They're great for priority
# queues where an item's priority may change and the priority queue needs to be reordered.
#
dictionary = {
    'a': 1,  # The key is 'a' and the value is 1
    'b': 2  # The key is 'b' and the value is 2
}

# To access a value in a dictionary, we use the corresponding key.
print(dictionary['b'])  # This will output: 2

# A dictionary can store different types of data as values.
dictionary2 = {
    'a': [1, 2, 3],  # list
    'b': "Hello",    # string
    'x': True,       # boolean
}

# You can also access items in the values if they are a sequence type like a list or string.
print(dictionary2['a'][2])  # This will output: 3, accessing the third element of the list associated with key 'a'

# A dictionary can also be a value inside a list or another dictionary.
my_list = [
    {
        'a': [1, 2, 3],  # This is a dictionary as a list element
        'b': "Hello",
        'x': True,
    },
    {
        'a': [4, 5, 6],  # Another dictionary as a list element
        'b': "list_2",
        'x': False,
    }
]

# We can access elements in the list and then elements in the dictionary.
print(my_list[0]['a'][2])  # This will output: 3, accessing the first dictionary in the list, then the value of key 'a', and then the third element in that list.
print(my_list[1]['b'])  # "list_2"

# What can we use as keys?
# Dictionary key needs to be immutable!  Numbers, booleans, strings etc. ok
# Lists and other datastructures that are mutable are not ok!
# Keys in a dictionary must be unique! Repeated values will overwrite the old one

# We might want to check whether a dictionary has a key

user = {
    'health': 32,
    'height': 181
}

# What if we want to check whether user an age value without throwing an error?

# Use the .get method on the dictionary

print(user.get('age'))  # None
print(user.get('height'))  # 181
print(user.get('age', 55))  # 55, Adds a default value if unavailable

user2 = dict(name='Tom')  # This way of creating dictionaries is not that common


# A Google search will show the other dictionary methods.

print('health' in user.keys())  # True -> checks the keys
print('health' in user.values())  # False -> checks the values

print(user.items())  # dict_items([('health', 32), ('height', 181)]) prints out the values in a tuple

print(user2.clear())  # Clears the dictionary inplace

user3 = user.copy()
print(user3)  # {'health': 32, 'height': 181}

print(user.pop('height'))  # 181, this pops the value and returns it
print(user)  # {'health': 32}
