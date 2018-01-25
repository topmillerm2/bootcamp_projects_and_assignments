#find and replace
value="It's thanksgiving day. It's my birthday, too!"
print value
print(value.find("day"))
# b = value.find("day", i +1)
# print(b)
result = value.replace("day", "month", 1)
print(result)

#max and min
x = [2,54,-2,7,12,98]
print(x)
print (max(x))
print (min(x))

#first and last in new list
y = ["hello",2,54,-2,7,12,98,"world"]
print [(y[0], y[len(y)-1])]

#sort and list in a list
z = [19,2,54,-2,7,12,98,32,10,-3,6]
print (z)
z.sort()
print (z)
#one option:
first_list = z[:len(x)/2]
second_list = z[len(x)/2:]
print "first_list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
#second option:
# w = [z[:len(y)/2+1]]
# z[:5] = w
# print(z)