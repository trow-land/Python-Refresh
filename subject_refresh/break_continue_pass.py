# Break exits the loop,
# continue skips the iteration
# pass is a null statement and is used when a statement is required syntactically

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break  # terminate the loop now
    print(number)  # 1 2 - This line will not run when number is 3

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        continue  # skip the rest of this iteration and continue with the next one
    print(number)  # 1 2 4 5

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        pass  # do nothing and continue to the next line
    print(number)  # 1 2 3 4 5

# pass can be used as a placeholder if you are still thinking about what to put in a for loop

