#lets say we want to measure the body mass of someone.. to do that google the 
#format for measuring body mass which is 
#bmi = (weight/(height * height)) * 10000
#say you measure for someone 

height = 55
weight = 52 

bmi = (weight/(height * height)) * 10000
print(bmi)

#what if i want to measure for 4 people?
#we can use def function

def calculate_bmi(height, weight):
    bmi = (weight/(height * height)) * 10000
    print(bmi)

calculate_bmi(162, 60)    
calculate_bmi(170, 88)
calculate_bmi(134, 65)
calculate_bmi(181, 54)

#what if we want to print different stuff for the individual function we're calling
#we have to take out

def calculate_bmi(height, weight):
    bmi = (weight/(height * height)) * 10000
 
calculate_bmi(162, 60)    
# calculate_bmi(170, 88)
# calculate_bmi(134, 65)
# calculate_bmi(181, 54)