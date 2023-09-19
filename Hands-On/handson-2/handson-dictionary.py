student1 = {"name":"Mark", "age":8, "class":5, "country":"Nigeria", "vaccinated":True, "blood_group":"0+"}
student2 = {"name":"James", "age":10, "class":4, "country":"Canada", "vaccinated":True, "blood_group":"0-"}
student3 = {"name":"Amaka",
            "age":15,
            "class":6,
            "country":"Canada",
            "Vaccinated":True,
            "blood_group":"0+"
            }
#values of a key in dict can be a list e.g studet2 = {"name":"mike", "cources":["aws", "tf", "azure"]}
students = [student1, student2, student3] #turn it to list
print(student1)
print(students) #it will output all the students infos in a list [{}]
print(students[1]) #to print just student 2 info
print(students[0:2]) #to access student1 & student2 info

#what if i have many things i can't count on the list, and i want to index from the last from left
#use -1 eg
# print(students[-1]) 
print(students[-1])
print(students[-2]) #this will print the second to d last

#TO ACCESS THINGS ON A PARTICULAR STUDENT DICTIONARY
print(student3["blood_group"]) #we just want to know the blood group of a particular student
#you can use get function
student2.get("blood_group") #to print this function, just wrap it with a print function
print(student2.get("blood_group"))

#to get student1 name using get function
print(student1.get("name")) 

#to replace student2 name from james to collins
student2["name"] = "Bako"
print(student2)
#we can use this to ass a key value too
print(student2.get("name"))
print(student2.keys()) #to print all the keys for student2
print(student2.values())



