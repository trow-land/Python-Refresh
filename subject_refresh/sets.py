# Sets - An unordered collection of unique objects
# In a set everything has to be unique

my_set = {1, 3, 4, 5, 6, 7}
print(my_set)  # {1, 3, 4, 5, 6, 7}

my_set = {1, 3, 4, 5, 6, 7, 7}
print(my_set)  # {1, 3, 4, 5, 6, 7}   / the duplicate number isn't printed

my_list = [1, 3, 4, 5, 6, 7, 7]
print(set(my_list))   # Removes any duplicates

# Sets do not support indexing
# print(my_set[0])  # Does not work
print(list(my_set))  # [1, 3, 4, 5, 6, 7]
print(list(my_set)[1])  # 3

print(3 in my_set)  # True
print(len(my_set))  # 6  Only counts the unique values


# Set methods

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))  # {1, 2, 3}

print(my_set.discard(5))  # None
print(my_set)  # {1, 2, 3, 4}

print(my_set.update(your_set))  # None
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.intersection(your_set))  # {4, 5}

print(my_set.isdisjoint(your_set))  # False (because of 4 and 5) Do they have anything in common? False = common, true = not in common

print(my_set.union(your_set))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, united the two sets removing the duplicates
print(my_set | your_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},  Shorthand version of the above

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set))  # True
print(my_set.issuperset(your_set))  # False

