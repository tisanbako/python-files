import boto3            #for connecting to aws

client = boto3.client('iam')     

users = ["jerry", "tisan", "bako", "bako_python"]  #added bako_python user i created ealier
for i in users: 
    print("Deleting an iam user with the name: ",i)
    response = client.delete_user(       
    UserName= i
    )

    #print("Result: ", response) as it returns none, so no need to pring