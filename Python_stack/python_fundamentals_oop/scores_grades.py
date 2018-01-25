def scores_grades(num):
    print "Scores and Grades"
    if random_num in range(60, 70):
        print "Score:", random_num, ";" "Your grade is D"
    if random_num in range(70, 80):
        print "Score:", random_num, ";" "Your grade is C"
    if random_num in range(80, 90):
        print "Score:", random_num, ";" "Your grade is B"
    if random_num in range(90, 100):
        print "Score:", random_num, ";" "Your grade is A"  
    print "End of the program.  Bye!"
import random
random_num = random.randint(60, 101)
scores_grades(random_num)


#book answer:

# import random

# def grade(reps):
#     print "Scores and Grades"
#     for x in range(0, reps):
#         score = random.randint(60, 101)
#         if score >= 60 and score <= 69:
#             print "Score: ", score,"; Your grade is D"
#         elif score >= 70 and score <= 79:
#             print "Score: ", score, "; Your grade is C"
#         elif score >= 80 and score <= 89:
#             print "Score: ", score, "; Your grade is B"
#         elif score >= 90 and score <= 100:
#             print "Score: ", score, "; Your grade is A"
#         else:
#             print "You failed"
#     print "End of the program.  Bye!"

# grade(10)