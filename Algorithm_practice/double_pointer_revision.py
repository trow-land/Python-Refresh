# Redoing the questions without checking to confirm understanding

# Find the Pair that Sums to a Target Value using two pointers
array = [1, 2, 3, 4, 6]
targ = 6


def find_pair(arr, target):
    left_pointer_index = 0
    right_pointer_index = len(arr) - 1

    while left_pointer_index < right_pointer_index:

        if arr[left_pointer_index] + arr[right_pointer_index] == target:
            return [arr[left_pointer_index], arr[right_pointer_index]]
        elif arr[left_pointer_index] + arr[right_pointer_index] < target:
            # sum is less than target therefore sum is increased by increasing left pointer index
            left_pointer_index += 1
        else:
            # sum is greater than the target so sum is reduced by decreasing right index
            right_pointer_index -= 1

    return "There is no pair within the array that satisfies"


print(find_pair(array, targ))


# Reverse a String using two pointers

sentence = "Hello, world!"

def reverse_string(string):

    string_converted = list(string)
    left_pointer_index = 0
    right_pointer_index = len(string_converted) - 1

    while left_pointer_index < right_pointer_index:
        temporary_letter = string_converted[left_pointer_index]
        string_converted[left_pointer_index] = string_converted[right_pointer_index]
        string_converted[right_pointer_index] = temporary_letter

        left_pointer_index += 1
        right_pointer_index -= 1

    reversed_string = "".join(string_converted)
    return reversed_string


print(reverse_string(sentence))


# Remove Duplicates using two pointers

arr = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5]


def remove_duplicated(array):
    array = sorted(array)

    left_pointer = 0
    right_pointer = 1

    while right_pointer < len(array):
        # print("In while loop")
        if array[right_pointer] == array[left_pointer]:
            # duplicate
            right_pointer += 1
        elif array[left_pointer] != array[right_pointer]:
            # print("here")
            left_pointer += 1
            array[left_pointer] = array[right_pointer]
            right_pointer += 1

    return array[:left_pointer + 1]


print(remove_duplicated(arr))

# Merge Two Sorted Arrays

arr1 = [1, 3, 5, 7, 9, 20, 30, 50]
arr2 = [2, 4, 6, 8, 9, 20]

def merge_arrays(array1, array2):

    array1_index = 0
    array2_index = 0

    new_array = []
    flag = True

    while flag:
        if array1_index < len(array1) and array2_index < len(array2):
            if array1[array1_index] <= array2[array2_index]:
                # append the smaller value first and then increment both
                new_array.append(array1[array1_index])
                new_array.append(array2[array2_index])
                array1_index += 1
                array2_index += 1
            else:
                new_array.append(array2[array2_index])
                new_array.append(array1[array1_index])
                array1_index += 1
                array2_index += 1
        else:
            flag = False

    if len(array1) > len(array2):
        new_array.extend(array1[array1_index::])
    elif len(array2) > len(array1):
        new_array.extend(array2[array1_index::])

    return new_array


print(merge_arrays(arr1, arr2))


# Palindrome Check: Check if a given string or array is a palindrome using two pointers.
string = "radar"
array = [1, 2, 3, 2, 1, 2]

def check_palindrome(input_data):
    left_pointer = 0
    right_pointer = len(input_data) - 1

    while left_pointer != right_pointer:
        if input_data[left_pointer] != input_data[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True


print(check_palindrome(string))
print(check_palindrome(array))



# Intersection of Two Arrays: Given two sorted arrays, find their intersection.

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 3, 5]

def find_intersection(array1, array2):

    array1_index = 0
    array2_index = 0

    intersection = []

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] > array2[array2_index]:
            # if array2 value is less than array1 counterpart then increase array2 index
            array2_index += 1
        elif array1[array1_index] < array2[array2_index]:
            array1_index += 1
        else:
            # array values are equal therefore they are intersecting so append to intersection array
            intersection.append(array1[array1_index])
            array1_index += 1
            array2_index += 1

    return intersection

print(find_intersection(arr1, arr2))

