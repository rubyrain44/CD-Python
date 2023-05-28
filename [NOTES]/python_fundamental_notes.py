PYTHON NOTES

#Python is a backend technology (server side) that is basically the middle man for the HTML and the database. In the HTTP Request/Response cycle, the site
#will ask for something from the database and Python is what allows it to retrieve that data and send it back to the site. It's language very closely
#resembles the English language.

What is a code block?
# A code block is a set of lines of code that belong together. For example, the first line of an if statement gives the condition, but the line(s) that 
# follow explain what we want to happen if the condition is true. Examples of code block keywords include:
    # - def (functions)
    # - if, elif, else (conditional statements)
    # - for, while (loops)
    # - Class (classes)
        x = 10
        if x > 50:
            print("bigger than 50")
        else:
            print("smaller than 50")

#Python has provided us with the pass statement for situations where we know we need the block statement, but we aren't sure what to put in it yet:
        class EmptyClass:
            pass

PRIMITIVE DATA TYPES:
#Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
    is_hungry = True
    has_freckles = False
#Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
    age = 35 # storing an int
    weight = 160.57 # storing a float
#Strings - literal text
    name = "Joe Blue"

COMPOSITE DATA TYPES:
#Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
    dog = ('Bruce', 'cocker spaniel', 19, False)
    print(dog[0])		# output: Bruce
    dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)
#Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
    empty_list = []
    ninjas = ['Rozen', 'KB', 'Oliver']
    print(ninjas[2]) 	# output: Oliver
    ninjas[0] = 'Francis'
    ninjas.append('Michael')
    print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
    ninjas.pop()
    print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
    ninjas.pop(1)
    print(ninjas)	# output: ['Francis', 'Oliver']
#Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
    empty_dict = {}
    new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
    new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
    new_person['hobbies'] = ['climbing', 'coding']
    print(new_person)    # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
    w = new_person.pop('weight')	# removes the specified key and returns the value
    print(w)    # output: 160.2
    print(new_person)    # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

COMMON FUNCTIONS:
#If we're ever unsure of a value or variable's data type, we can use the type function to find out.
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

#For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11 

NUMBERS: 
int  num = 25
float  dec = 4.2
log  print(num)
type check  print(type(dec))
conversion  import random
            rand_num = random.randint(2,5)

#There are 3 basics types of numbers in Python.
    int - whole numbers, positive or negative.  ex. 35
    float - decimal numbers, positive or negative.  ex. 4.2
    complex - are a part of the real number system and are often referenced with the letter j.  ex. 1 + 3j.

#If you are unsure on which type a number is, you can use the type() to view the object type of any object.
    print(type(24))
    print(type(3.9))
    print(type(3j))

#All Python objects have data type methods we can use to convert number types from one to another.
    int_to_float = float(35)
    float_to_int = int(44.2)
    int_to_complex = complex(35)
    print(int_to_float)
    print(float_to_int)
    print(int_to_complex)
    print(type(int_to_float))
    print(type(float_to_int))
    print(type(int_to_complex))

#Python does not have a built in random number generator, use the random module instead.
    import random
    print(random.randint(2,5)) # provides a random number between 2 and 5

STRINGS:

#Strings are any sequence of characters (letters, numerals, ~($/}\#, etc.) enclosed in single or double quotes. We can display a string like this:
    print("this is a sample string")

#There are multiple ways that we can print a string containing data from variables. The first is by adding a comma after the string, followed by the 
# variable. Note that the comma is outside the closing quotation mark of the string. The print() function inserts a space between elements separated by a 
# comma.
    name = "Zen"
    print("My name is", name)

#The second is by concatenating the contents into a new string, with the help of +.
    name = "Zen"
    print("My name is " + name)

#We may find ourselves wanting to change a value's data type from one type to another. Python doesn't know how to add a string and a number, but it can 
#add two strings together, so if we can cast the number as a string, then we will be able to "add" the two values together, like so:
    print("Hello " + 42)			# output: TypeError
    print("Hello " + str(42))		# output: Hello 42

#Another example may be receiving a string input from a user that we want to treat as a number:
    total = 35
    user_val = "26"
    total = total + user_val		# output: TypeError
    total = total + int(user_val)		# total will be 61

#F-Strings (Literal String Interpolation)
# Python 3.6 introduced f-strings for string interpolation. To construct a f-string, place an f right before the opening quotation. Then within the string, 
# place any variables within curly brackets.
    first_name = "Zen"
    last_name = "Coder"
    age = 27
    print(f"My name is {first_name} {last_name} and I am {age} years old.")

#Prior to f-strings, string interpolation was accomplished with the .format() method. If you're searching online, you will likely find code snippets using 
# this method. To use it, type out the full string, replacing any words that will get their values from variables with {}. Then call the format method on the
# string, passing in arguments in the order in which they should fill the {} placeholders. Here's an example:
    first_name = "Zen"
    last_name = "Coder"
    age = 27
    print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
    # output: My name is Zen Coder and I am 27 years old.
    print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
    # output: My name is 27 Zen and I am Coder years old.

# There is an even older method of string interpolation that you may come across when troubleshooting or researching, so you should know about it. Rather 
# than curly braces, the % symbol is used to indicate a placeholder, a %s for a string and %d for a number. After the string, a single % separates the string
# to be interpolated from the values to be inserted into the string, like so:
    hw = "Hello %s" % "world" 	# with literal values
    py = "I love Python %d" % 3 
    print(hw, py)
    # output: Hello world I love Python 3
    name = "Zen"
    age = 27
    print("My name is %s and I'm %d" % (name, age))		# or with variables
    # output: My name is Zen and I'm 27

# We've seen the format method, but there are several more methods that we can run on a string. Here's how to use them:
    x = "hello world"
    print(x.title())
    # output:
    "Hello World"

    # The following is a list of commonly used string methods:
    string.upper(): returns a copy of the string with all the characters in uppercase.
    string.lower(): returns a copy of the string with all the characters in lowercase.
    string.count(substring): returns number of occurrences of substring in string.
    string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
    string.find(substring): returns the index of the start of the first occurrence of substring within string.
    string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
    string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
    string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

LISTS:

# In Python, the elements of a list do not have to be of the same data type. A list can be a mixture of any Python data types, including, tuples, strings, 
# numeric, and even a list itself (a list within a list). An example:
    ninjas = ['Rozen', 'KB', 'Oliver']
    my_list = ['4', ['list', 'in', 'a', 'list'], 987]
    empty_list = []

# Another cool feature of lists in python is that you can combine them together and duplicate values fairly easily, by using the + and * operators. If you 
# 'add' lists together, it will create a new list that contains all the values of both of the arrays! Likewise, if you 'multiply' a list by a whole number it
# will copy all of the values that many times, and make a new list with all the copied values. Consider the example below:
    fruits = ['apple', 'banana', 'orange', 'strawberry']
    vegetables = ['lettuce', 'cucumber', 'carrots']
    fruits_and_vegetables = fruits + vegetables
    print(fruits_and_vegetables)
    salad = 3 * vegetables
    print(salad)

    LIST MANIPULATION:

drawers = ["documents", "envelopes", "pens"]    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

# When dealing with code, but especially arrays or lists in particular, it is crucial to have a good understanding of what part of a statement 
# gets read and evaluated by the interpreter (or compiler as the case may be) before it can be executed. Whenever an indexed value in a list is on the 
# right-hand side of the =, the assignment operator, the interpreter has to go fetch that raw value from memory. The left hand side is indicating the 
# location in memory only, not the value.
    location = raw value

    SLICING:
#It's also useful to know that Python uses the following syntax: [:] to return a copy of some portion of the list, constrained by specified indices. This 
#is called slicing and it can be useful if you want to:
#     Use a copy of the list so you don't have to change the original
#     Only use a portion of a list.
#     The starting index and ending index should be separated by the : character. 
    words = ["start","going","till","the","end"]
    # Sub-ranges (portions) of the list
    print(words[1:]) # prints ['going', 'till', 'the', 'end']
    print(words[:4]) # prints ['start', 'going', 'till', 'the']
    print(words[2:4]) # prints ['till', 'the']

    # Making a copy of a list
    copy_of_words = words[:]
    copy_of_words.append("dojo") # only appends to the copy
    print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
    print(words) # prints ['start', 'going', 'till', 'the', 'end']

    BUILT IN FUNCTIONS:
#Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequence types, including 
# dictionaries, strings and tuples. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly 
# used sequence function:
    my_list = [1, 'Zen', 'hi']
    print(len(my_list))  # output 3

    Examples:
    len(sequence) returns the length (number of items) in a sequence.
    max(sequence) returns the highest value in a sequence.
    min(sequence) returns the lowest value in a sequence.
    sorted(sequence) returns a sorted sequence

    list.append(value) appends a value to the end of the list.
    list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
    list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
    list.reverse() reverses the order of the elements, in place.*
    list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place, meaning it changes that same array, instead of 
                returning a new array.    
        my_list = [1,5,2,8,4]
        my_list.pop()
        print(my_list)  # output: [1,5,2,8]

TUPLES:

# A Tuple is a container for a fixed sequence of data objects. The name comes from the Latin suffix for multiples: double, triple, quadruple, quintuple. 
# Tuples are sequences, just like lists. The only difference is that tuples can't be changed -- that is, tuples are immutable. Also, while lists are defined 
# using square brackets, tuples use parentheses. Creating a tuple is as simple as declaring different comma-separated values. Optionally you can put these 
# values between parentheses.
    tuple_data = ('physics', 'chemistry', 1997, 2000)
    tuple_num = (1, 2, 3, 4, 5 )
    tuple_letters = "a", "b", "c", "d"

CONDITIONALS:

# Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.  These statements control the flow of how 
# our code is executed by the interpreter.  In Python, the keywords for conditional statements are if, elif, and else. Here are some examples:
    x = 12
    if x > 50:
        print("bigger than 50")
    else:
        print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
    x = 55
    if x > 10:
        print("bigger than 10")
    elif x > 50:
        print("bigger than 50")
    else:
        print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    if x < 10:
        print("smaller than 10")
    # nothing happens, because the statement is false

==  Checks if the value of two operands are equal: 
    1 == 2 => False
    1 == 1 => True

!=	Checks if the value of two operands are not equal:
    1 != 2 => True
    1 != 1 => False

>	Checks if the value of left operand is greater than the value of right operand:
    1 > 2 => False
    2 > 1 => True

<	Checks if the value of left operand is less than the value of right operand:
    1 < 2 => True
    2 < 1 => False

>=	Checks if the value of left operand is greater than or equal to the value of right operand:
    1 >= 2 => False
    2 >= 2 => True

<=	Checks if the value of left operand is less than or equal to the value of right operand:
    1 <= 2 => True
    2 <= 2 => True

and	Checks that each expression on the left and right are both True:
    (1 <= 2) and (2 <= 3) => True
    (1 <= 2) and (2 >= 3) => False
    (1 >= 2) and (2 >= 3) => False

or	Checks if either the expression on the left or right is True:
    (1 <= 2) or (2 >= 3) => True
    (1 <= 2) or (2 <= 3) => True
    (1 >= 2) or (2 >= 3) => False

not	Reverses the true-false value of the operand:
    not True => False
    not False => True
    not 1 >= 2 => True
    not 1 <= 2 => False
    not (1 <= 2 and 2 >= 3)  => True
    not 1 <= 2 and 2 >= 3 => False

LOOPS WITH RANGE():

#Only One Argurment
for i in range(5):
    print(i)
    # Output:
        # 0
        # 1
        # 2
        # 3
        # 4
i starts at 0 by default
exits loop when i is 5 (prints 4 but not 5!)
i increases by 1 each time by default

#Two Arguements
for i in range(2, 7):
    print(i)
    # Output:
    #     2
    #     3
    #     4
    #     5
    #     6
i starts at 2
exits when i is 7 (prints 6 but not 7!)
i increases by 1 each time by default

#Three Arguements
for i in range(2, 16, 3):
    print(i)
    # Output:
    #     2
    #     5
    #     8
    #     11
    #     14
i starts at 2
exits when i is 16 or larger than 16
i increases by 3 each time

# Note that if you need to specify an increment other than +1, all three arguments are required. You may also start at a large number and go down! 
# To decrement (think going backwards) the step will be a negative number to indicate i will get smaller each iteration.
    for x in range(0, 10, 2):
        print(x)
    # output: 0, 2, 4, 6, 8
    for x in range(5, 1, -3):
        print(x)
    # output: 5, 2

FOR AND WHILE LOOPS:

    FOR:
# Since a loop can be used on any sequence, you can access each value of a string individual with loop.
    for x in 'Hello':
        print(x)  # output: 'H', 'e', 'l', 'l', 'o'

# If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not 
# interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list 
# directly!
    my_list = ["abc", 123, "xyz"]
    for i in range(0, len(my_list)):
        print(i, my_list[i])  # output: 0 abc, 1 123, 2 xyz
    # OR 
    for v in my_list:
        print(v)  # output: abc, 123, xyz

    WHILE:
# While loops are another way of looping while a certain condition is true.
    count = 0
    while count <= 5:
        print("looping - ", count)
        count += 1

# The basic syntax for a while loop looks like this:
    while <expression>:
        # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

    ELSE:
# There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something 
# if that happens? We can then use an else statement with our while loop. Yes, that is right, else in a loop.
    y = 3
    while y > 0:
        print(y)
        y = y - 1
    else:
        print("Final else statement")

# Note that this else code section is only executed if the while loop runs normally and its conditional is false (whether we never entered the while loop, 
# or we did but eventually the conditional changed from true to false). If instead our while loop is exited prematurely because of a break or return 
# statement, then the else code section will never be executed.

    BREAK:
# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while 
# and for loops. The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop. When loops are nested, 
# a break will only exit from the innermost loop.
    for val in "string":
        if val == "i":
            break
        print(val)
    # output: s, t, r
# Notice that when the loop got to the letter "i", we stopped looping.

    CONTINUE:
# The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the 
# remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop. The continue statement is very useful 
# when you want to skip specific iteration(s), but still keep looping to the end.
    for val in "string":
        if val == "i":
            continue
        print(val)  # output: s, t, r, n, g -Notice, no i in the output, but the loop continued after the i

    y = 3
    while y > 0:
        print(y)
        y = y - 1
        if y == 0:
            break
    else:  # only executes on a clean exit from the while loop (i.e. not a break)
        print("Final else statement")  # output: 3, 2, 1

FUNCTIONS:

# A function is a named block of code that we can execute to perform a specific task. More simply, a function is a list of instructions that we can run at 
# any time and as many times as we would like. If we find something that we seem to be using over and over again, it might be best to have a way to 
# streamline the process. A function:
    has a name
    takes in parameters (parenthesis required, parameters optional)
    perform a series of instructions
    return something afterwards (will return None if there is no explicit return statement)

# The def keyword signifies the declaration of a function. This indicates that the following code is a function and assigns a name to that function, so we 
# can call it later. Parameters are inputs the function is expecting and appear inside the parenthesis that follow the function name.
    def add(a,b):	# function name: 'add', parameters: a and b
        x = a + b	# process
        return x	# return value: x

    PARAMETERS & ARGUMENTS:
# We have declared a function with the def keyword, named it add, and specified that it takes two inputs (parameters). If this is all we have in our file, 
# nothing would actually appear to happen if we ran it. To actually run the function, we must execute it by invoking or calling it. This is done outside of 
# the function using the function name followed by (). Inside the parenthesis are any values (arguments) the function is expecting as input.
    new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
    print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# Once invoked, a function can give us an output. Some functions take an input and some functions don't give us an output. Even if no output is produced, 
# the code inside the function can alter the program - this is called a side effect. Based upon what we learned above, a function that doesn't return 
# anything would produce no output!

# We define the input of functions using parameters. Functions can have as many parameters as we need, including 0. Here we've defined the say_hi function 
# with one parameter called name:
    def say_hi(name):
        print("Hi, " + name)
    # Now, we can invoke this function by calling its name and passing in the correct number of arguments:
    # invoking the function 3 times, passing in one argument each time
    say_hi('Michael')
    say_hi('Anna')
    say_hi('Eli')

    RETURN:
# So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can use 
# later in our program. The following concept is critical in understanding how to use functions correctly in your code: It is very important to remember the 
# following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.
    def say_hi(name):
        return "Hi " + name
    greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
    print(greeting) # this will output 'Hi Michael'

# Returning a value from a function allows us to store that value in a variable. In this example, we invoked the say_hi function with "Michael" and set it 
# to the greeting variable. When we print greeting we see that it contains the returned value of the say_hi function - "Hi Michael".

    def add(a, b):
        x = a + b
        return x
    sum1 = add(4,6)
    sum2 = add(1,4)
    sum3 = sum1 + sum2
# If you guessed 10, 5, and 15, respectively, good job! sum1 was set to the return value of the add function invoked with 4 and 6 as arguments. 
# Similarly, sum2 was set to the return value of invoking add with 1 and 4. The variable sum3 contains the sum of sum1 and sum2 which is 15. Storing 
# these return values in variables allows us to use the results of our functions throughout the rest of our program. Functions can return any of the data 
# types - strings, numbers, lists, tuples, dictionaries and even other functions!

    DEFAULT PARAMETERS:
# With the functions we've written so far, we've had to provide the exact number of arguments specified when calling the function. However, if we'd like to 
# allow some of the parameters to be optional to the caller of the function, we can set defaults. Take the following function as an example. The purpose of 
# the function is to take a name and a number and print "good morning {some_name}" to the terminal the given number of times. If no name or number is given, 
# the name is blank and the number is 2, respectively.

    # set defaults when declaring the parameters
    def be_cheerful(name='', repeat=2):
        print(f"good morning {name}\n" * repeat)
    be_cheerful()    # output: good morning (repeated on 2 lines)
    be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
    be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
    be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
    be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
    # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
    be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

DEBUGGING:

# Debugging is an important skill in any language. We're going to reiterate a few principles your instructor may have already spoken about. It's important 
# to be able to understand what is happening when your code runs. You'll go a long way when debugging your code using just print statements. Although 
# print statements will be especially key as you learn to code, they're going to be an important tool for the rest of your coding career. Without some 
# way of visualizing your code, it's easy to lose track of what's going on. 

# Learning to use print statements to their greatest advantage and how to correctly search for answers are not one-time skills. You can't just do this 
# assignment and move on, or assume that we'll tell you when you need to use these skills. What we've introduced here is a skill set you'll use for every 
# assignment in all of your code forever. Now is the time to start practicing, because the better you get, the more self-sufficient you become.

DICTIONARIES:

# A Dictionary is another mutable sequence type that can store any number of Python objects, including other sequence types. Dictionaries consist of pairs 
# (called items) of keys and their corresponding values. While this data structure is known as a dictionary in Python, you'll see the same structure 
# referred to as an associative array or hash table in other languages. In general, hash table is the most generic term.
    A dictionary is an unordered collection of objects.
    Values are accessed using a key (typically a string).
    A dictionary can shrink or grow as needed.
    The contents of dictionaries can be modified.
    Dictionaries can be nested.
    Sequence operations such as slice cannot be used with dictionaries.

    KEYS:
    # Keys are typically strings
    # Keys are not in any sort of order, as dictionary values are NOT stored sequentially in memory.
    # Dictionaries ONLY have keys.

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionarycopy
# Notice: the keys in the example above are all strings, but the values are a variety of types. Generally you will only use strings for your keys. 
# You can think of them as a label for the stored value.

    Adding New Key-Value Pairs:
# Dictionaries do not have a .append() method. You can add new values by setting a new key much like you would a variable. 

    #literal notation
    person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
    capitals = {} #create an empty dictionary then add values
    capitals["svk"] = "Bratislava"
    capitals["deu"] = "Berlin"
    capitals["dnk"] = "Copenhagen"
    copy
In the examples above, we created two dictionaries in two different ways:
# 1) Using literal notation. The key-value pairs are enclosed by curly brackets. The pairs are separated by commas. The first value of a pair is a key, which 
# is followed by a colon character and a value. The "first" string is a key and the "Ada" string is a value.
# 2) Creating an empty dictionary and adding some values. The keys are inside the square brackets, the values are located on the right side of the assignment.
    my_dict["some_string"] = some_value

    Changing or Updating Values:
# Each key in a dictionary must be unique. If you make an assignment using an existing key as the index, the old value associated with that key is 
# overwritten by the new value. You can use this characteristic to an advantage in order to modify an existing value for an existing key. 
    person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
    # Adds a new key value pair for email to person
    person["email"] = "alovelace@codingdojo.com"
    # Changes person's "last" value to "Bobada"
    person["last"] = "Bobada"
    print(person)
    # Notice that the syntax above is the same for adding a new value as it is for updating a value.

    Testing for an Existing Key:
# Sometimes you may want to test if a key already exists in the dictionary to know whether to add an initial value or replace an existing value.
    if some_key in my_dictionary:
        # update the value

    if "email" not in person:
        person["email"] = "newemail@email.com"
    else:
        print("Would you like to replace your existing email?")

    Accessing Values:
# To access the values of a dictionary, you can use the familiar square brackets along with the key to obtain its value.
    print(person["first_name"])
    full_name = person["first_name"] + " " + person["last_name"]copy

    Removing Values:
# There are 2 ways to remove a key:value pair from a dictionary. 
    value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
    del capitals['dnk'] # will delete the key, and not return anythingcopy

    Multi-Line Syntax Too:
# You can write any dictionary's key-value pairs on multiple lines to make it easier to read, which is very useful for larger dictionaries. For example 
# the following dictionary..
    person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}copy
    ..can also be written like so:

    person = {
        "first": "Ada", 
        "last": "Lovelace", 
        "age": 42, 
        "is_organ_donor": True
    }

    Common Built-in Functions and Methods:
# Python includes the following standalone functions for dictionaries:
    len() - give the total length of the dictionary.
    str() - produces a string representation of a dictionary.
    type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.

# Here are some very useful Python dictionary methods:
    .clear() - removes all elements from the dictionary
    .get(key, default=None) - A safe way to get a value, if the key might not exist. Returns the value for the specified key or None 
        (or a value you specify) if the key is not in the dictionary.
    .update(pairs_to_update) - Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.

LOOPS & DICTIONARIES:

# Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.
    my_dict = { "name": "Noelle", "language": "Python" }
    for each_key in my_dict:
        print(each_key)  # output: name, language

# That means if we want the values of our dictionary, we might do something like this:
    my_dict = { "name": "Noelle", "language": "Python" }
    for each_key in my_dict:
        print(my_dict[each_key])  # output: Noelle, Python

# Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator.
    capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
    
    # another way to iterate through the keys
    for key in capitals.keys():
        print(key)  # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

    #to iterate through the values
    for val in capitals.values():
        print(val)  # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond

    #to iterate through both keys and values
    for key, val in capitals.items():
        print(key, " = ", val)  # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

NESTING:

# Nesting is also allowed in dictionaries. In other words, dictionaries may contain lists and tuples as well as other dictionaries. Likewise, lists may 
# contain dictionaries. All of these may be many levels deep! In this module you'll become more familiar with how to manipulate nested lists and 
# dictionaries.

    # List of dictionaries
    users = [
        {"first": "Ada", "last": "Lovelace"}, # index 0
        {"first": "Alan", "last": "Turing"}, # index 1
        {"first": "Eric", "last": "Idle"} # index 2
    ]

    # Dictionary of lists
    resume_data = {
        #        	     0           1           2
        "skills": ["front-end", "back-end", "database"],
        #                0           1
        "languages": ["Python", "JavaScript"],
        #                0              1
        "hobbies":["rock climbing", "knitting"]
    }

# To access a value in a nested data structure take a look at how you would access the first user's last name. 

print(users[0]["last"]) # prints Lovelace

# Tip: Pay very close attention to which kind of brackets you're looking at in the nested structure. If it starts with {, it's the start of a dictionary 
# and you'll need a key, to access something one level further into it. If it starts with [, it's a list, and you'll need an index to go one level further 
# into it.

OOP (Object Oriented Programming)

# Here's the syntax for creating a class that we want to call User:
    class User:
        pass    # we'll fill this in shortly

# And here's how we create a new instance of our class:
    michael = User()
    anna = User()

# A constructor is a function that contains instructions for making a new instance of a class, in this case a new user. It's kind of like 
# when you turn in your completed medical forms to the receptionist. In Python, this is a special function called the __init__ method. 
# When called, this method will designate some space in memory to store the user, and then assign the first name, last name and age by 
# executing the lines below:

# declare a class and give it name User
    class User:		
        def __init__(self):
            self.first_name = "Ada"
            self.last_name = "Lovelace"
            self.age = 42

# You can use the syntax Your_Class_Name() to create and then store a new instance of a class, in this case,  User() to make and save a new 
# user in memory, but remember, you'll need a variable to store it! For the most part, you'll create your object instances outside the class 
# definition, in the outer or global scope. 

# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
    user_ada = User()
    print(user_ada.first_name) # prints Ada

# In this example we're just storing two strings and a number together in the variable user_ada, similar to how a dictionary stores 
# multiple pieces of data in one place, they are stored as one data type, type User. And you can access them with dot-notation:  
# user_ada.first_name

