# x = [ [5,2,3], [10,8,9] ] 

# x[1][0] = 15
# print(x)

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name'] = 'Bryant'
# print(students)

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# sports_directory['soccer'][0]='Andres'
# print(sports_directory)

# z = [ {'x': 10, 'y': 20} ]

# z[0]['y']=30
# print(z)

################################################################

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for student in students:
#         print_str = ""
#         for key, value in student.items():
#             print_str += (f'{key} - {value}, ')
#         print(print_str[:-2]) #slice function to remove end

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

################################################################

# students = [
#         {'first_name' : 'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(key_name, students):
#     for fn in students:
#         print(fn[key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

################################################################

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)

# 7 LOCATIONS
# San Jose

# 8 INSTRUCTORS
# Michael


# length_key = len(dojo['locations'])
#     print(length_key, "LOCATIONS")
#     for key, val in dojo.items()
#         print(key, val)
#     length_key = len(dojo['instructors'])
#     print(length_key, "INSTRUCTORS")