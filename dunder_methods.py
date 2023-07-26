# Define the Toy class
class Toy():
    # Constructor method for Toy
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name': 'Tom',
            'has_pets': False
        }

    # str method for Toy, returns colour of the Toy
    def __str__(self):
        return f'{self.colour}'

    # len method for Toy, returns 5
    def __len__(self):
        return 5

    # call method for Toy, returns "yes?"
    def __call__(self):
        return "yes?"

    # getitem method for Toy, returns item from my_dict
    def __getitem__(self, i):
        return self.my_dict[i]

# Instantiate Toy
action_figure = Toy('red', 0)

# Using str method
print(action_figure.__str__())  # red

# Using str built-in function
print(str(action_figure))  # red

# Using len built-in function
print(len(action_figure))  # 5

# Using call method
print(action_figure())  # yes?

# Using getitem method
print(action_figure['name'])  # Tom
