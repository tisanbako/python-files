import requests

#to list users 
response = requests.get("https://reqres.in/api/users?page=2")
print(response)
print(response.json())