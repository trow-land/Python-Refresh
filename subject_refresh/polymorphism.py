# Polymorphism

# We are creating a game with different types of Users: knights, archers, and wizards

# This is the parent class. All user types will inherit from this class.
class User():
    # Every User, regardless of type, has the ability to sign in. This method simulates that.
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")


# Wizard is a type of User, so it inherits from User
class Wizard(User):
    # The constructor method for a Wizard. It's called when you create a new Wizard.
    # Each Wizard needs a name and a power level.
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        # self.email = email  # Inefficient!!!
        super().__init__(email)

    # Wizards attack with their power
    def attack(self):
        print(f"Attacking with a power of {self.power}")


# Archer is also a type of User, so it also inherits from User
class Archer(User):
    # Similar to Wizard, the Archer has a name and a number of arrows when created.
    def __init__(self, name, num_arrows, email):
        self.name = name
        self.num_arrows = num_arrows
        super().__init__(email)

    # Archers attack with arrows
    def attack(self):
        print(f"Attacking with arrows! Arrows left = {self.num_arrows}")


# Knight is another type of User, so it inherits from User as well
class Knight(User):
    # Similar to Wizard and Archer, the Knight has a name and a sword attack power when created.
    def __init__(self, name, sword_attack, email):
        self.name = name
        self.sword_attack = sword_attack
        super().__init__(email)

    # Knights attack with their sword
    def attack(self):
        print(f"Attacking with sword attack of power {self.sword_attack}")

def character_attack(character):
    character.attack()  # Dont currently know the type of user - only that it has an attack method


# Here we're creating an instance of each type of User.
wizard1 = Wizard("Gandalf", 50, "gandalf@gmail.com")  # Gandalf is a Wizard with a power of 50
archer1 = Archer("Legolas", 100, "legolas@hotmail.com")  # Legolas is an Archer with 100 arrows
knight1 = Knight("Aragorn", 100, "aragon@hotmail.com")  # Aragorn is a Knight with a sword attack power of 100

# Now we're making Gandalf attack
wizard1.attack()
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True  - because wizard is a subclass of user
print(isinstance(wizard1, object))  # True - because all classes get methods from the object base class that python comes with

# Using the new function to attack with each type of User.
character_attack(wizard1)  # Gandalf attacks with power
character_attack(archer1)  # Legolas attacks with arrows
character_attack(knight1)  # Aragorn attacks with sword

# The SAME function is able to take different types of object and perform the appropriate action
# based on the objets class type


# Introspectioon   this is what the . does when listing the available methods and attributes
print(dir(wizard1))




