#to make api call we nned to import the request module
#if we don't have the module, we need to install it.. eg pip3 install requests


import requests 


#list all users
response = requests.get("https://reqres.in/api/users?page=2")       #what kind of request? could be get, post,put,delete etc and past th dns and resquest link in the bracket
print(response)       #you will get 200 which means ok (succesful call)
print(response.json())      #to print the actual data as api is in json

print()                  #just to put a gap between the two blocks of code
#list single users
response1 = requests.get("https://reqres.in/api/users/2")       #what kind of request? could be get, post,put,delete etc and past th dns and resquest link in the bracket
print(response1)       #you will get 200 which means ok (succesful call)
print(response1.json()) 


print()


#creat
reply = requests.post("https://reqres.in/api/users", {
    "name": "morpheus",
    "job": "leader"
})  #for post(create) we need to pass json key/value data in th bracket
print(reply)    #reponse 201  HTTP 201 Created success status response code indicates that the request has succeeded and has led to the creation of a resource.