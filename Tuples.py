# Tuples are just like immutable lists

my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z'  # This will give an error because you cant change the elements

print(5 in my_tuple)  # True
print(my_tuple)  # (1, 2, 3, 4, 5)

# Why do we need tuples?
# If you don't need to change the list then tuples can be used, improved safety and efficiency but less flexible

# An example of a good use of a tuple would be lat/long for a pickup point at uber

new_tuple = my_tuple[1:2]
print(new_tuple) # (2,)  (A Tuple with a single item in it)

x,y,z,*other = (1,2,3,4,5,5,5)
print(x)  # 1
print(y)  # 2
print(z)  # 3
print(other)  # [4, 5, 5, 5]

print(other.count(5))  # 3
print(other.index(4))  # 0
print(len(other))  # 4
