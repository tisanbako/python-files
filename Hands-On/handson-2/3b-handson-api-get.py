import requests

#to list users 
#what if we want to call this many times? we creat a function 


# response = requests.get("https://reqres.in/api/users?page=2")
# print(response)
# print(response.json())

#EX1
def get_users():
    print("request: Getting all users....")
    response = requests.get("https://reqres.in/api/users")  #remove ?page=2 from https://reqres.in/api/users?page=2 as it means that you want users in just page 2
    print("ResponsCode: ", response)
    print("responseBody: ", response.json())


get_users()

#this will print just what we have on top. but to get get the users and further 
#process the data, we need to put it in a variable when calling it eg
print()

#EX2
def get_users():
    print("request: Getting all users....")
    response = requests.get("https://reqres.in/api/users")  #remove ?page=2 from https://reqres.in/api/users?page=2 as it means that you want users in just page 2
    #print("ResponsCode: ", response)
    #print("responseBody: ", response.json())
    return response.json()


users = get_users()
print(users)

print()

#we can further use the rerun object

#EX3
def get_users():
    print("request: Getting all users....")
    response = requests.get("https://reqres.in/api/users")  #remove ?page=2 from https://reqres.in/api/users?page=2 as it means that you want users in just page 2
    #print("ResponsCode: ", response)
    #print("responseBody: ", response.json())
    return response.json()


users = get_users()
print(users)
for i in users["data"]:   #data is the what the list?dict contains
    print(i["email"], "sending email" )
   
print()

#EX4
#to get indivual users
def get_users(user_id):
    print("Request: Get user with id: ", user_id)
    result = requests.get(f"https://reqres.in/api/users/{user_id}")  #take out the 2 from https://reqres.in/api/users/2 as it says to show page two. so no matter what value you put when calling it, it will always show page 2
    print("ReturnCode: ", result)
    print("ReturnBody: ", result.json())
    return result


get_users(1)     #whatever id number you put here, that's what it will print
get_users(3)     #whatever id number you put here, that's what it will print
