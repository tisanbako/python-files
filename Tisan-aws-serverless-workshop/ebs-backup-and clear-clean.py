#Get all EBS vOLUME
#Filter unused (available) volume
#Take a snapshot
#Delete volume
#First creat and ec2 instance and then create two volumes


import boto3
import time 

def lambda_handler(event, context):  #copied from lambda
    client = boto3.client('ec2')  

    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ]
            },
        ],
    )
    for i in response["Volumes"]:
        print(i["VolumeId"])
        print()  
        print("Creating snapshot for the volume ...", i["VolumeId"] )
        response = client.create_snapshot(   
            VolumeId=i["VolumeId"]
        )
        time.sleep(5)  
        print("Deleting available volumes", i["VolumeId"])
        response = client.delete_volume(
            VolumeId=i["VolumeId"]
        #DryRun=True|False not required... you can take this line off.
    
    )
        


