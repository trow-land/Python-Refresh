import random
class Enemy:

    def __init__(self, name ="Enemy", hit_points=0, lives=1):
        self._name = name  # Can use regex expression to refactor the replacement fields
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._hit_points = 0
            self._lives -= 1

            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)  # This is the recommended way to call methods in the superclass

    # The super() function is used to give access to methods and properties of a parent or sibling class.
    # The super() function returns an object that represents the parent class.

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you!".format(self))


class Vampyre(Enemy):

    def __init__(self, name, lives=3, hit_points=12):
        super().__init__(name=name)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage//4)


