# Functions

# Functions must be defined at the beginning because the interpreter goes line by line
# Below uses positional parameters
def raise_to_the_power(number, power):
    result = number**power

    return result


print(raise_to_the_power)  # <function raise_to_the_power at 0x000002683A9D04A0>, Shows the location in memory
print(raise_to_the_power(5, 2))  # 25

# Below calls the function using keyword arguments
print(raise_to_the_power(power=4, number=4))  # 256


def raise_power(number=5, power=2):
    result = number**power

    return result


print(raise_power())  # 25, We can call the function without params and the default values will be used
answer = raise_power()
answer2 = raise_power(raise_power(5, 2), 2)  # The function can be used within the function
print(answer2)

