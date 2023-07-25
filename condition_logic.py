

is_old = False
has_license = False

if is_old and has_license:
    print("Congratulations you can drive!")
elif is_old and not has_license:
    print("You need to get a license to drive!")
elif not is_old and has_license:
    print("Sorry you are not allowed to drive - you are too young!")
else:
    print("You are both too young and don't have a license")


# Truthy and Falsy values
if 'hello':  # 'hello' is a non-empty string, so it's truthy
    print('This is truthy')

if []:  # An empty list is falsy
    print('This is falsy')
if 0:  # An empty list is falsy
    print('This is falsy')
if None:  # An empty list is falsy
    print('This is falsy')
else:
    print('The list is empty and thus falsy')



# Ternary Operator (Also called a Conditional Expression

# Can someone message someone on facebook (for example)
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)  # message allowed



# Short Circuiting - or Keyword



