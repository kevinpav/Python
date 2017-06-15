# Part I
# Given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a program that outputs:
#
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
# for student in students:
#     print student['first_name'], student['last_name']

##

# Now, given the following dictionary:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Get the key: value pairs from the users dictionary
for type, people  in users.items():
    print type
    pIndex = 1  # Index used for each person
    # Now process each person in a particular person type
    for person in people:
        print pIndex, person['first_name'], person['last_name'], "-", len(person['first_name'] +person['last_name'])
        pIndex += 1
