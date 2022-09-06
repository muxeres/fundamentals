# variable declaration
    # Data Types
        # Primitive
num1 = 42 #Numbers
num2 = 2.3 #Numbers
boolean = True #Boolean
string = 'Hello World' #Strings
# log statement
    # List 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
    # Diccionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
    # Tuples
fruit = ('blueberry', 'strawberry', 'banana')
# type check
print(type(fruit))
# List access value
print(pizza_toppings[1])
# List add value
pizza_toppings.append('Mushrooms')
# Diccionary access value
print(person['name'])
# Diccionary change value
person['name'] = 'George'
# Diccionary add value
person['eye_color'] = 'blue'
# Tuples access value
print(fruit[2])
# conditional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# for loop
for x in range(5):#start
    print(x)
for x in range(2,5):#start-stop
    print(x)
for x in range(2,10,3):#start-stop-increment
    print(x)
x = 0 # start
# while loop
while(x < 5):#stop
    print(x)
    x += 1#increment
#remove elements 
pizza_toppings.pop()#dont remove any element
pizza_toppings.pop(1)#remove element position 1

print(person)
#remove key and value key of the dictionary
person.pop('eye_color')
print(person)
#for loop,break,continue
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):#x parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#4 argument

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) -NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
# print(boolean)
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'