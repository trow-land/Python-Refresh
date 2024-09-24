""" A rescue dog simulator to practice python OOP


To Do: More complex attributes (health, weight, friendliness), another method (train_pet),
add random events in walk that can affect attribute values

Add a parent Pet class
Add a cat subclass

"""

class Pet:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = int(age)

    def feed_pet(self):
        self.hunger -= 75
        self.happiness += 30

        self.happiness = min(100, self.happiness)
        self.hunger = max(0, self.hunger)

        self.print_stats()
    
    

class Dog(Pet):

    def __init__(self, name, age) -> None:
        super().__init__(name, age)  
        self.hunger = 30  # 0 is full and 100 is hungry
        self.happiness = 100 # 100 is happy and 0 is unhappy
        self.energy = 80 # 100 is max energy, 0 is low energy
    
    def walk_dog(self, walk_length:int):
        # walk length in minutes
        self.energy -= walk_length * 0.2 * self.age
        self.hunger += 0.5 * walk_length
        self.happiness += 0.5 * walk_length
        
        self.happiness = min(100, self.happiness)
        self.hunger = min(100, self.hunger)
        self.energy = max(0, self.energy)

        self.print_stats()

    def cuddle_dog(self):
        self.happiness += 50

        self.happiness = min(100, self.happiness)

        self.print_stats()
        

    def time_passes(self, time):
        # 6 hours passes in the simulator
        # time in hours
        print(f"\n{time} hours passes by....")

        self.hunger += 8 * time
        self.happiness -= 2 * time
        self.energy += 18 * time / self.age  # Dogs regain energy slower as they age

        self.happiness = max(0, self.happiness)
        self.hunger = min(100, self.hunger)
        self.energy = min(100, self.energy)
        self.print_stats()


    def print_stats(self):

        self.state = (self.hunger, self.happiness, self.energy)
        print(f"\n\n{self.name}'s stats: ")
        print("(Hunger, Happiness, Energy) : ", self.state)


class Cat(Pet):

    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.hunger = 20  # 0 is full and 100 is hungry
        self.happiness = 50 # 100 is happy and 0 is unhappy
        self.energy = 50 # 100 is max energy, 0 is low energy

    def groom_cat():
        pass

    def play_with_cat(self, toy):
        pass

    def time_passes(self, time):
        self.hunger += 3 * time
        self.happiness -= 8 * time
        self.energy += 12 * time / self.age

        self.happiness = max(0, self.happiness)
        self.hunger = min(100, self.hunger)
        self.energy = min(100, self.energy)

    def print_stats(self):

        self.state = (self.hunger, self.happiness, self.energy)
        print(f"\n\n{self.name}'s stats: ")
        print("(Hunger, Happiness, Energy) : ", self.state)


def get_valid_walk_time():

    while True:
        try:
            walk_length = int(input("How many minutes are you going to walk the dog? "))
            if walk_length <= 0:
                print("Please enter a valid walk length (1 - 120 minutes)")
            else:
                return walk_length
        except ValueError:
            print("Invalid input: Please enter a valid input number")


def adopt_pet(dog_list, cat_list):
    # This function will be used to adopt a new cat or dog and to input their name and age
    choice = input("Would you like to adopt a pet? (yes/no) \n").lower()

    while choice == 'yes':
        try:
            animal = input("Would you like to adopt a cat or dog? ").lower()
            if animal == 'dog':
                name = input("What pet are you going to chose from the dog rescue centre? \nName = ")
                age = input(f"How old is {name}? \nAge = ")
                dog = Dog(name, age)
                dog.print_stats()
                dog_list.append(dog)  # Add to dog list
                
            elif animal == 'cat':    
                name = input("What pet are you going to chose from the cat rescue centre? \nName = ")
                age = input(f"How old is {name}? \nAge = ")
                cat = Cat(name, age)
                cat_list.append(cat)  # Add to cat list
                cat.print_stats()

            choice = input("Would you like to adopt another pet? (yes/no) ").lower()  # Continue adopting pets if user wants

        except ValueError:
            print("Please input valid values for age.")


        print(f"\nCongratulations on adopting {name.capitalize()}! They are going to have a great life in your home!")
        print("To quit the simulation type 'quit' when asked for an action")



dog_list = []
cat_list = []

action = ""
#adopt_pet(dog_list, cat_list)

print(dog_list)
print(cat_list)


dog1 = Dog("Dennis", 3)
dog2 = Dog('Gary', 4)

dog_list.append(dog1)
dog_list.append(dog2)
# name = input("What pet are you going to chose from the dog rescue centre? \nName = ")
# age = input(f"How old is {name}? \nAge = ")

# dog = Dog(name, age)
# dog.print_stats()

# print(f"\nCongratulations on adopting {name.capitalize()}! They are going to have a great life in your home!")
# print("To quit the simulation type 'quit' when asked for an action")


while action != 'quit':
    action = input("\nWhat action would you like to take? (walk, feed, cuddle) ")

    permitted_actions = ['walk', 'feed', 'cuddle', 'rest' 'adopt pet', 'quit']

    for i, pet in enumerate(dog_list):
        print(f'Dog index {i} | Name - {pet.name} | Age - {pet.age}' )

    for i, cat in enumerate(cat_list):
        print(f'Cat index {i} | Name - {pet.name} | Age - {pet.age}' )

    while action != 'rest':

        pet = input("What pet (index) would you like to interact with? \n")

        if 'cat' in pet:
            print("Here")





# def choose_action():

#     while action != 'quit':

#         action = input("\nWhat action would you like to take? (walk, feed, cuddle) ")

#         permitted_actions = ['walk', 'feed', 'cuddle', 'adopt pet', 'quit']

#         if action in permitted_actions:

#             if action == 'walk':   
#                 dog.walk_dog(get_valid_walk_time())
#             elif action == 'feed':
#                 dog.feed_pet()
#             elif action == 'cuddle':
#                 dog.cuddle_dog()

#         while True:
#             try:
#                 time = int(input("How much time should pass before next action? "))
#                 dog.time_passes(time)
#                 break
#             except ValueError:
#                 print("Please input a valid number of whole hours")


    







