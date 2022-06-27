# x = [ [ 5,2,3], [15,8,9]]
# students = [
#     {'frist_name': 'Michael', 'last_name' : 'Bryant'},
#     {'first_name': 'John', 'last_name' : 'Rosales' }
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry' ],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x' : 15, 'y' : 30} ]


# DONE


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(somelist):
#     print(somelist[:4])

# iterateDictionary(students)

def iterateDictionary2(somelist):
    txt = students
    x = txt.split(",")
    print(x[:4])
    print(somelist)

iterateDictionary2(students)