#odds in a range
for i in range(1, 1000):
    if i%2 == 1:
        print (i)
#or:
# for count in range(1, 1001, 2):
#     print count

#multiples of 5 in range
for i in range(5, 1000001):
    if i%5 ==0:
        print(i)
#or:
# for count in range (5,1000001, 5)
#     print count

# sum of values in a list
a = [1, 2, 5, 10, 255, 3]
print sum(a)
#or:
# my_numbers = [1, 2, 5, 10, 255, 3]
# sum = 0
# for i in my_numbers:
#     sum += i
# print sum

#average of values in a list
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
    
