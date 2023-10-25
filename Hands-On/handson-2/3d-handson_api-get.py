#from 3b (EX4) one thing object that is dynamic is user_id but another thing 
#that is dynamic is the website of the api (https://reqres.in)
#to make the wesite dynamic across all blocks of code, we should make it 
#a variable as BASE_URL



import requests

BASE_URL = "https://reqres.in"      #btw we can put this i ssm as the API is a sensitive info


#EX1
def get_users():
    print("request: Getting all users....")
    response = requests.get(f"{BASE_URL}/api/users")  #remove ?page=2 from https://reqres.in/api/users?page=2 as it means that you want users in just page 2
    #print("ResponsCode: ", response)
    #print("responseBody: ", response.json())
    return response.json()


users = get_users()
print(users)

print()

#we can further use the rerun object


#EX2
def get_users():
    print("request: Getting all users....")
    response = requests.get(f"{BASE_URL}/api/users")  #remove ?page=2 from https://reqres.in/api/users?page=2 as it means that you want users in just page 2
    #print("ResponsCode: ", response)
    #print("responseBody: ", response.json())
    return response.json()


users = get_users()
print(users)
for i in users["data"]:   #data is the what the list?dict contains
    print(i["email"], "sending email" )
   
print()


#EX3
#to get indivual users
def get_users(user_id):
    print("Request: Get user with id: ", user_id)
    result = requests.get(f"{BASE_URL}/api/users/{user_id}")  #take out the 2 from https://reqres.in/api/users/2 as it says to show page two. so no matter what value you put when calling it, it will always show page 2
    print("ReturnCode: ", result)
    print("ReturnBody: ", result.json())
    return result


get_users(1)     #whatever id number you put here, that's what it will print
get_users(3)     #whatever id number you put here, that's what it will print

print()

def create_user(user_info):
    print(f"Request: Create user with info, {user_info}")
    outcome = requests.post(f"{BASE_URL}/api/users, {user_info}")
    print("ResponseCode: ", outcome)
    print("ResponseBody: ", outcome.json())
    return outcome.json()

create_user({
    "name": "morpheus",
    "job": "leader"
})    