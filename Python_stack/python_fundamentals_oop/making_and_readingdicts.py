myinfo = {'name': 'Michael', 'age': '26', 'country of birth': 'The United States', 'favorite language': 'Python'}
for key, value in myinfo.items():
    print "My", key, "is", value
    #or:
    print "My {} is {}".format(key, value)