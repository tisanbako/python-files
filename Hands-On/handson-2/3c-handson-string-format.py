name = "vamsi"
price = 100
age = 28
items_bought = ["pen", "chocolate", "cake"]

# shopping = [name, price, age, items_bought] #['vamsi', 100, 28, ['pen', 'chocolate', 'cake']]
# print(shopping) 
# print()
# print(name, price, age, items_bought)  #vamsi 100 28 ['pen', 'chocolate', 'cake']


#to print it with key value pair we need to wring the key in a str eg

print(f"Name:{name}, Price:{price}$, Age:{age}, Item_bought:{items_bought}")

msg = f"hello vamsi"
print(msg)

value = 10
api_endpoint = f"https://reqres.in/api/users/{value}"
print(api_endpoint)