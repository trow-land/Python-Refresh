x = 10  # A global variable


def update_global_var():
    global x  # Telling Python that we want the global x
    x = 20  # Now we're updating the global x
    print(f"Inside function, x is {x}")  # Inside function, x is 20


update_global_var()
print(f"Outside function, x is {x}")  # Outside function, x is 20


def outer():
    x = 10  # This is a variable in the outer function

    def inner():
        nonlocal x  # We're telling Python that we want the x that's in outer(), not a new local x
        x = 20  # Now we're updating that x
        print(f"Inside inner function, x is {x}")  # Inside inner function, x is 20

    inner()
    print(f"Inside outer function, x is {x}")  # Inside outer function, x is 20


outer()
