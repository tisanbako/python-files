#client uses functions


import boto3

#here we are using default session

ec2 = boto3.client("ec2", region_name = "us-east-1")  #for same account but specify the region

#lets say we want to describe the instance #put it in a var response
response = ec2.describe_instances (InstanceIds=[
        "i-020f877852d48ee44",
    ],)
print(response)
 