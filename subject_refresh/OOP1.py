# OOP

# Class names should be capitalised.
# Class names should also be written in camel case (ClassName) NOT snake case (class_name)

class BigObject:   # Class definition
    # code
    pass


object1 = BigObject()  # Instantiating the class
object2 = BigObject()  # Instantiating the class
object3 = BigObject()  # Instantiating the class

print(type(object1))

# Instances of a class will get instantiated


class PlayerCharacter:
    # Class object attribute  - NOT dynamic - they are static
    membership = True

# The def __init__ gets called upon every instantiation
    def __init__(self, name='anonymous', age=0):  # dunder method -> at the top of a class this is a constructor method
        if age > 18:
            # Attributes - are dynamic (specific to each object/instantiation)
            self.name = name  # This code will run when the class gets instantiated
            self.age = age
# self refers to the player character
# self.name = the parameter name
# removing the self prevents the player1 object getting the name

    def run(self):
        print('run')

    def shout(self):
        print(f"My name is {self.name}!")

    # We can use class methods without instantiating a class (not used as often)
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # @staticmethod  # Does not have access to the class


player1 = PlayerCharacter("Tom", 30)
player2 = PlayerCharacter("Dennis", 2)

print(player1.name)  # Tom
print(player1.age)  # 30
print(player2.name)  # Dennis

player1.jump = 2
print(player1.jump)  # 2

# help(player1)  # This show the whole class blueprint

player1.shout()  # My name is Tom!

