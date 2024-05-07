from time import *
import random as r

def mistake(para_test, user_test):
    error = 0
    for i in range(len(para_test)):
        try:
            if para_test[i] != user_test[i]:
                error += 1 
        except:
            error = error + 1
    return error

def speed_time(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(user_input) / time_roundoff
    return round(speed)

test = ["My Name is Muhammad Waqas. We are going to test the Typing Speed. So let's see what is going to happen.",
        "We are living in Jalal Pur Sharif.",
        "Master Waqas is learning Python."] #Test Paragraphs
test1 = r.choice(test)
print("*****Typing Speed Calculator*****")
print(test1)
print()
print()

time_1 = time()
test_input = input("Enter : ")
time_2 = time()

print("Speed : ", speed_time(time_1, time_2, test_input), "words / second") #Speed Checker
print("Error : ", mistake(test1, test_input)) #Mistakes Finder