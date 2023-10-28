import boto3            #for connecting to aws

client = boto3.client('iam')     #what service so we want ot communicate with

#if we want to creat many things in a file eg ec2 with iam, we rename our variable to iam_client = client = boto3.client('iam')
#print(dir(client))   #to see the actions we can do with iam using boto3 client
response = client.create_user(       #what do we want to do with iam... response can be anything
    UserName="bako_python"
)

print(response)