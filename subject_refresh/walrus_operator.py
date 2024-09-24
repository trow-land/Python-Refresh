# The walrus operator assigns variables as part of an expression

import random


while (number := random.randint(0, 10)) != 5:
    print(f"The random number is {number}, let's try again.")

print("Finally, the random number is 5!")
