#FOR LOOP - to iterate over sequence of collcetion of items (tupple, str, list, set)
#while loop - to interate when condition is true. while something exist keeo looping

count = 0

while count <5:

    print("infinity")  #crt c to stop
    #use break to stop it or use a statement to stop it eg below
    count = count + 1  #everytime it iterates value of count increaes by 1


# #if we can only allow more than ten people in a house 

total_capacity = 10
current_capacity = 0

while current_capacity < total_capacity:
    print("Enter inside")
    current_capacity += 1

#my-assignment - what if i want to see the difference of number of people in 
#the place and how many i have to fill 

total_capacity = 10
present_capacity = 0
capacity_to_fill = 0

while present_capacity < total_capacity:
    capacity_to_fill = total_capacity - present_capacity
    present_capacity += 1
    print(f"you have {capacity_to_fill} more people to fill")
   