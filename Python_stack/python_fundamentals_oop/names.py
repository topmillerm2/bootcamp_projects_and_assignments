# part1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for data in students:
    print data['first_name'], "", data['last_name']

#part2
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
count = 0
print "Students"
for value in users['Students']:
    count += 1
    end_num = len(value['first_name']+ value['last_name'])
    print count, "-", value['first_name'], "", value ['last_name'], "-", end_num
count = 0
print "Instructors"
for value in users['Instructors']:
    count += 1
    print count,"-", value['first_name'], "", value ['last_name'],"-", end_num