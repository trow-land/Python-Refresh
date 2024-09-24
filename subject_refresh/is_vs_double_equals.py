# is vs ==

print(1 == 1)  # True, because the values are equal
print('hello' == 'hello')  # True, because the values are equal


a = [1, 2, 3]
b = a
print(a is b)  # True, because a and b are pointing to the same list in memory

c = [1, 2, 3]
print(a is c)  # False, because c is a different list stored in a different location in memory

a = [1, 2, 3]
b = a
c = list(a)  # make a copy of a

print(a == b)  # True
print(a is b)  # True

print(a == c)  # True
print(a is c)  # False, because they have a different location in memory


