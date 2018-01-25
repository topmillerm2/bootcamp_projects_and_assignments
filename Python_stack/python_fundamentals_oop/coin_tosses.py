import random
def coin_tosses(attps):
    print ("Starting the program...")
    head_sum = 0
    tail_sum = 0
    attempts = 1
    for i in range(0, attps):
        new_toss = random.randint(0,1)
        if new_toss==1:
            head_sum += 1
            print ("Attempt #", attempts,": Throwing a coin...It's a head!... Got", head_sum, "head(s) and", tail_sum,"tail(s) so far")    
        if new_toss==0:
            tail_sum += 1  
            print ("Attempt #", attempts,": Throwing a coin...It's a tail!...Got", head_sum, "head(s) and", tail_sum,"tail(s) so far")
        attempts += 1
    print ("Ending the program, thank you!")


coin_tosses(5000)


