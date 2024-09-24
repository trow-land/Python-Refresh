
my_list = [1, 2, 3, 4, 5, 5, 6]

for item in my_list:
    print(item)  # Prints all the items in the list

# Iterables
# List, dictionary, tuple, set, string etc.
# iterate: one by one check each item in the collection

user = {
    'name': "Tom",
    'age': 30,
    'can_swim': True,
}

for item in user:
    print(item)
    # name
    # # age
    # # can_swim

for item in user.items():
    print(item)
    # ('name', 'Tom')
    # ('age', 30)
    # ('can_swim', True)

for item in user.values():
    print(item)
    # Tom
    # 30
    # True

for item in user.keys():
    print(item)
    # name
    # age
    # can_swim

for key, value in user.items():   # Very common pattern
    print(key, value)
    # name Tom
    # age 30
    # can_swim True

for k, v in user.items():   # often shortened to
    print(k, v)
    # name Tom
    # age 30
    # can_swim True


# Range
for number in range(0, 100):
    print(number)  # prints numbers from 0 - 99 i.e 100 loops

# When we do not need a specific variable just use an _
# It shows to other programmers that you are not bothered about the variable it is just for the loop
for _ in range(0, 10):
    print(_)  # prints 0 - 9

for _ in range(0, 10, 2):  # The third parameter is the step again
    print(_)  # Prints 0 2 4 6 8


# Enumerate -> useful if you need the index counter of the item your looping through
for i, char in enumerate("Hello"):
    print(i, char)
    # 0 H
    # 1 e
    # 2 l
    # 3 l
    # 4 o

for i, char in enumerate(list(range(100))):
    if i == 50: 
        print(f"The index of 50 is: {i}")
