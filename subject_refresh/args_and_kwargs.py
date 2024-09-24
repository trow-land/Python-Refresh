# The *args parameter allows the function to accept any number of positional arguments.
# When used inside the function, args is a tuple of all the positional arguments.
def super_func(*args):
    print(args)  # (1,2,3,4,4,5) - when run on the input below
    # The sum function can operate on the tuple of arguments, adding them all together.
    return sum(args)


# The function with 6 positional arguments
print(super_func(1, 2, 3, 4, 4, 5))  # 19, the *args allows us to include as many arguments as we want


# The **kwargs parameter allows the function to accept any number of keyword arguments.
# When used inside the function, kwargs is a dictionary where the keys are the argument names and the values are the argument values.
def super_sum_func(*args, **kwargs):
    print(args, kwargs)  # (1, 2, 3, 4, 4, 5) {'num1': 5, 'num2': 10}
    total = 0
    # kwargs.values() gives us all the values of the keyword arguments, which we can then add to the total.
    for items in kwargs.values():
        total += items
    # The total sum of all positional and keyword arguments is returned.
    return sum(args) + total


# The function is called with 6 positional arguments and 2 keyword arguments.
print(super_sum_func(1, 2, 3, 4, 4, 5, num1=5, num2=10))  # 34


def example_func(**kwargs):
    print(kwargs)


example_func(a=1, b=2, c=3)  # prints the kwargs dictionary to illustrate the point


# The below function shows the convention for which order to write the arguments in a function definition
# Rule: params, *args, default parameters, **kwargs
def example_function(arg1, arg2, *args, default_arg1="default1", default_arg2="default2", **kwargs):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("*args: ", args)
    print("default_arg1: ", default_arg1)
    print("default_arg2: ", default_arg2)
    print("**kwargs: ", kwargs)


example_function(1, 2, 3, 4, 5, default_arg1="non-default1", default_arg2="non-default2", keyword1=6, keyword2=7)




