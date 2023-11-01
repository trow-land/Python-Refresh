# Find the Pair that Sums to a Target Value using two pointers
array = [1, 2, 3, 4, 6]
targ = 6


def brute_force(arr, target):
    left_index = 0
    right_index = 1

    while left_index != len(arr):
        if arr[left_index] + arr[right_index] == target:
            return [left_index, right_index]
        else:
            if right_index != len(arr) - 1:
                right_index += 1
            elif right_index == len(arr) - 1:
                left_index += 1
                right_index = left_index + 1


print(brute_force(array, targ))  # [1, 3]


def double_pointer(arr, target):
    left_index = 0
    right_index = len(arr) - 1

    arr = sorted(arr)

    while left_index != right_index:
        if arr[left_index] + arr[right_index] == target:
            return [left_index, right_index]
        elif arr[left_index] + arr[right_index] < target:  # Sum is too small
            left_index += 1
        elif arr[left_index] + arr[right_index] > target:  # Sum is too big
            right_index -= 1


print(double_pointer(array, targ))  # [1, 3]

# Reverse a String using two pointers

sentence = "Hello, world!"


def reverse_str(string):
    string_list = list(string)  # Convert to a list as strings are immutable
    left_index = 0
    right_index = len(string) - 1

    while left_index != right_index:
        # switch the characters in place
        temp = string_list[left_index]
        string_list[left_index] = string_list[right_index]
        string_list[right_index] = temp

        left_index += 1
        right_index -= 1

    string = "".join(string_list)  # Convert list back to a string using the join functions

    return string


print(reverse_str(sentence))  # !dlrow ,olleH

# Remove Duplicates using two pointers

arr = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5]


def remove_duplicates(arr):

    arr = sorted(arr)

    left_pointer = 0
    right_pointer = 1

    while right_pointer != len(arr):
        if arr[left_pointer] == arr[right_pointer]:  # duplicate
            right_pointer += 1
        else:  # unique
            left_pointer += 1  # Move to the next position
            arr[left_pointer] = arr[right_pointer]  # Copy unique element here
            right_pointer += 1  # Move right_pointer to next element

    unique_array = arr[:left_pointer + 1]

    return unique_array


print(remove_duplicates(arr))  # [0, 1, 2, 3, 4, 5]


# Merge Two Sorted Arrays

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]


def merge_arrays(array1, array2):

    array1 = sorted(array1)
    array2 = sorted(array2)

    left_pointer_index = 0
    right_pointer_index = 0

    new_array = []
    min_length = min(len(array1), len(array2))

    while left_pointer_index < len(array1) and right_pointer_index < len(array2):
        if array1[left_pointer_index] <= array2[right_pointer_index]:
            new_array.append(array1[left_pointer_index])
            left_pointer_index += 1
        else:
            new_array.append(array2[right_pointer_index])
            right_pointer_index += 1

    # Append whatever is left if arrays are not equal length
    new_array.extend(array1[left_pointer_index:])
    new_array.extend(array2[right_pointer_index:])

    return new_array


print(merge_arrays(arr1, arr2))


