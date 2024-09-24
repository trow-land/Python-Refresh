
some_list = ['a', 'v', 'v', 'g', 'y', 'q', 'a']

duplicates = []
next_index = 1

for item in some_list:
    for value in some_list[next_index:]:
        if item == value:
            duplicates.append(item)
    next_index += 1

print(duplicates)

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
