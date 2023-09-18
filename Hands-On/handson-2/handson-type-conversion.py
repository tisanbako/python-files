#There are two types of "type conversion"
# 1. IMPLICIT CONVERSION: the type that python interpreter for us.
# whatever data that +-*/ a decimal number will get the result of as float
number1 = 10
number2 = 2.0

print(number1+number2)

print(type(12.0))  #eventhought 12 is same as 12.0, it's still a float

#EXPLICIT TYPE CONVERSION: This are the ones we convert ourselves for meet certain data type criteria for AP1 etc

number3 = "100"

print(number3)

print(type(number3)) #string

#Now lets say you want it to be int, you will need to use the convert function

converted_number3 = int(number3) #to convert to str to int
print(converted_number3)
print(type(converted_number3))

#EXPLICIT CAN BE USED ON INPUT FUNCTIONS TOO

name = input("what is your name? ")
print("welcome", name)
print(type(name))


age = input("Enter yout age in years: ")
print(age)
print(type(age))
#print(age+5) #this will pass an error message as input funtion see's all data as string, 
#so whatever age eg 20 is seen as a string by the input function and we are trying to add it to int 5
#best thing to is to change age to int using the converted function
age_converter = int(age)
print(int(age_converter+5))

#or we can from line 38 just convert directly intead of having three line lines 38-40

