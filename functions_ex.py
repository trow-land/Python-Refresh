# Make a function to check a drivers age with an input and positional argument


#Answer 1 - using input
def check_driver_age():
    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


#Answer 2 - using input
def checkDriverAge(age):
    print("Your age is: ", age)
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


check_driver_age()
checkDriverAge(21)