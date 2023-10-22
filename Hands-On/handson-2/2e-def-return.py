#in Function, we can find the solution in the function and print the result 
#somwwhere else by using the Return statement


def greet(name):
    print("hello", name)
    return
greet("jerry")

#return statement terminates  and control of the program 
# goes back to where it's called. eg

def my_name(name1):
    print("hello", name1)
    return
    print("this won't print", jerry) #this will not print because the return function is a breaker

my_name("jerry")  #This will print hello jerry

def calculate_bmi(height, weight):
    bmi = (weight/(height * height)) * 10000
    return bmi

height = 162
weight = 50

bmi = calculate_bmi(height, weight)
print(bmi)

#or better still, we can change the variable while calling it 
def calculate_bmi(height, weight):
    bmi = (weight/(height * height)) * 10000
    return bmi

answer = calculate_bmi(162, 52)
print(answer)



def calculate_bmi(height, weight):
    bmi = (weight/(height * height)) * 10000
    return 200  #this will return 200 on every call.

answer = calculate_bmi(162, 52)   
print(answer)      #this will print 200
answer2 = calculate_bmi(140, 20) 
print(answer2)       #this will print 200
 
 