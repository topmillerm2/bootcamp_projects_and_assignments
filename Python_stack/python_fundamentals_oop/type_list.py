l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

current_tester = n
str_cont = "String:"
sum1 = 0
i = 0
while i< len(current_tester):    
    if isinstance(current_tester[i], str):
        str_cont += current_tester[i]+" " 
    elif isinstance(current_tester[i], int):
        sum1 += current_tester[i]
    elif isinstance(current_tester[i], float):
        sum1 += current_tester[i]
    i+=1
# curr_test = type(type(current_tester[i]))
# print curr_test
# if curr_test == str:
#     print "The list you entered is of string type"
# elif curr_test == int:
#     print "The list you entered is of integer type"
# elif curr_test == int and str and float:
#     print "The list you entered is of mixed type"
    
print str_cont
print sum1

#book answer:
# mixed_list = ['magical unicorns',19,'hello',98.98,'world']
# integer_list = [1,2,3,4,5]
# string_list = ["Spiff", "Moon", "Robot"]

# def identify_list_type(lst):
#     new_string = ''
#     total = 0

#     for value in lst:
#         if isinstance(value, int) or isinstance(value, float):
#             total += value
#         elif isinstance(value, str):
#             new_string += value

#     if new_string and total:
#         print "The array you entered is of mixed type"
#         print "Sting:", new_string
#         print "Total:", total
#     elif new_string:
#         print "They array you entered is of string type"
#         print "String:", new_string
#     else:
#         print "The array you entered is of number(float or int) type"
#         print "Total", total
# print identify_list_type(mixed_list)
# print identify_list_type(integer_list)
# print identify_list_type(string_list)

