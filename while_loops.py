# While loops


# infinite loops -> the condition is never met

# i = 0
# while 0 < 50:
#     print(i)

i = 0
while i < 50:
    print(i)  # prints 0 - 49
    i += 1
else:
    print("Done with all of the work")

# Sometimes the else statement is not needed
i = 0
while i < 50:
    print(i)  # prints 0 - 49
    i += 1
print("Done with all of the work")

# While loops are really flexible
# For loops are simpler and read better

# While loops are better if you do not know how many times you want to loop
password = ''
while password != 'secret':
    password = input('Please enter the secret password: ')
print('Access granted!')


# While True and break can also be used to cause an infinite loop until a condition is met
while True:
    password = input('Please enter the secret password: ')
    if password == 'secret':
        break






