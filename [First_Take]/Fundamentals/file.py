num1 = 42 #integer
num2 = 2.3 #float
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #tuples
print(pizza_toppings[1]) #sausage
pizza_toppings.append('Mushrooms') #adds to end
print(person['name']) #string
person['name'] = 'George' #changes person name to george
person['eye_color'] = 'blue' #adds the entire key value pair to the dictionary
print(fruit[2]) #banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#condtional
#It's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#condtional
#It's a long word!

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
#condtional
#error? x doesnt fit a for statement
#0, x=1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value
#['Pepperoni', 'Jalepenos', 'Cheese']

print(person)
person.pop('eye_color') #delete value
print(person)
#{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#condtional

def print_hello_ten_times(): #function
    for num in range(10):
        print('Hello')

print_hello_ten_times() 
#for loop

def print_hello_x_times(x): #function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#for loop

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#for loop


"""
Bonus section
"""

# print(num3) 72
# num3 = 72
# fruit[0] = 'cranberry' ('cranberry', 'strawberry', 'banana')
# print(person['favorite_team']) key error: favorite_team
# print(pizza_toppings[7]) index error list index out of range
#   print(boolean) true
# fruit.append('raspberry') add value ('blueberry', 'strawberry', 'banana', 'raspberry')
# fruit.pop(1) attribute error tuples has no attribute pop