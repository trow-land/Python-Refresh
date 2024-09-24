# String is text

print("This is a string")
print(type("This is a string"))

username = 'boxer'
password = 'secret'


# ''' Allows you to do multiline strings
long_string = '''
Look out!
0 . 0
********
'''

print(long_string)

first_name = "Tom"
last_name = "Rowland"

name = first_name + " " + last_name
print(name)

# String Concatenation - adding strings together

print("Hello " + "Tom")
# print("Hello " + 5)  # This will get a type error and fail to compile

print("Hello " + str(5))  # converts the int to a string and prints "Hello 5"

a = str(100)  # converts int to string
b = int(a)  # converts string back to int
c = type(b)  # prints out the type of the variable b
print(c)  # <class 'int'>


# Escape Sequence

# weather = 'It's sunny  # will not compute because of the early '
weather = "It's sunny"
print(weather)
weather = 'It\'s sunny'   # This is the escape sequence \
print(weather)

the_weather = "\tIt\'s is \"kind of\" sunny! \n Remember sun cream!"
print(the_weather)

# Most programming languages use these escape sequences




#### Formatted Strings

name = "Johnny"
age = 55

print("Hi " + name)
print("Hi " + name + ". You are " + str(age) + " years old")
print("Hi", name, ". You are ", age, "years old")
print("Hi {}. You are {} years old".format(name, age))

print(f'Hi {name}. You are {age} years old')




#### String indexing
selfish = "me me me"
print(selfish[0:2]) # me


number = "0123456789"
# [start:stop:step]
print(number[0:9])  # 0 - 8
print(number[0:9:2])  # 02468
print(number[2:])  # 23456789

print(number[::1])  # start at 0, end at the end with a step of 1

print(number[-1])  # start at the end = 9

print(number[::-1])  # 9876543210
print(number[::-2])  # 97531


### Immutability

string = "012203342"
print(string)
string = "dfwsdsadasdas"  # The string can be reassigned
print(string)  # dfwsdsadasdas
# string[0] = "M"  ## will give an error as strings are immutable

string = "M" + string[1:]  # Mfwsdsadasdas
print(string)

