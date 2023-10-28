import boto3            #for connecting to aws

client = boto3.client('iam')     

users = ["jerry", "tisan", "bako"] #put the names of users you want to create in a variable

#user for look to iterare the creation 
for i in users: 
    print("creating an iam user with the name: ",i)
    response = client.create_user(       
    UserName= i
    )

    print("Result: ", response)