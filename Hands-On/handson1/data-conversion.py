#we can change datat type in two ways.
#1. 

price = "100"
print (type(price))

data_change = int(price) #CHANGE THE DATA TYPE
print (type(data_change))
print(data_change - 40)

#2 to change ad add, subtract to something eg line 14
age = input ("how old are you")
print(age) 
print (type (age)) #python still see's the output of age as string to change it to int
print (int(age)+5)
