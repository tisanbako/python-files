fruits = ["apple","kiwi", "grapes", "watermelon"]
cars = ["Toyota", "Honda", "bmw", "Tesla"]

marks = [75, 40, 30, 63]

custom_list = ["Tisan", 100, True, None] #in phython, you can put any data type in a list unlike other languages like jave

print(cars)

print(fruits)

print (marks)

print(custom_list)

print(type(fruits))  #list

#len(fruits) #to show us the length (number of items)on the list of fruits
#len function can't print. to print, we need to wrap it in print function
print(len(fruits)) #to get the length #4

print(fruits[1]) #kiwi indexing

print(cars[2]) #504 indexing

#there are many python functions to manipulate/work with a list
#open python interactive run python3 enter
#run the function dir([]) #give list [] as a function
#ignore the functions that starts with __gfghd__ and check the last ones starting from 'append' to the end 'sort'
#here we can use these functions to edit the list..
#eg 'reverse' function for the lists of fruits
#google python reverse function example 
#exit and 

fruits.reverse() # reverse the order of list elements using reverse function
print(fruits) #['watermelon', 'grapes', 'kiwi', 'apple'] from ['apple', 'kiwi', 'grapes', 'watermelon']

# EX2. create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
prime_numbers.reverse()
print(prime_numbers)


# lets use sort functionality for cars
cars.sort()
print(cars)

#use append (to  add a single item to certain collection types) function for cars

cars.append("ferrari") #it won't take more than one string eg ("ferrari", "mecedes") it only takes one value
print(cars)

#use insert mode : to add An element of any type (string, number, object etc.)
cars.insert(1, "504")
print(cars)
#Note.. these functions doesn not not support between instances of 'int' and 'str'
#so it won't work for custom_list
fruits.insert(0, "guava")
print(fruits)

#to replace using insert function
fruits[0] = "agbalumo"
print(fruits)


#remove function: The remove() method takes a single element as an argument and removes it from the list
marks.remove(63) #Removes the first item with the specified value
print(marks)

#clear function- to remove everything on a list
cars.clear()
print(cars)

courses = ["aws", "python", "terraform", "git"]
print(courses[1])
print(courses[-1])
#accessing subsets 
print(courses[0:2]) #numbers on the left index from 0, numbers on right index from 1
print(courses[2:4])
print(courses[0:4])


#CHECKOUT MORE FUCTIONS AND TRY THEm
