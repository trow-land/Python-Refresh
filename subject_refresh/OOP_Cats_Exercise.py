#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("paws", 5)
cat2 = Cat("Mortisha", 10)
cat3 = Cat("Cribs", 4)


# 2 Create a function that finds the oldest cat
def find_oldest():

    oldest_cat = cat1.name
    if cat2.age > cat1.age:
        oldest_cat = cat2.name
        if cat3.age > cat2.age:
            oldest_cat = cat3.name

    return oldest_cat


# 3 Print out: "The oldest cat is "name", and they are x years old.".

print("The oldest cat is ", find_oldest(), "and they are ", max(cat1.age, cat2.age, cat3.age), " years old.")