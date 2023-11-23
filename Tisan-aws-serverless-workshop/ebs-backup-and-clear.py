#Get all EBS vOLUME
#Filter unused (available) volume
#Take a snapshot
#Delete volume
#First creat and ec2 instance and then create two volumes

import boto3
import time 

client = boto3.client('ec2')  #print(dir(client)) to see all the operations we can do with this

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
#print(response)
for i in response["Volumes"]:
    print(i["VolumeId"])
    print()  #for readability
#now that you got the volume ids (2) now go copy the code for creating snapshot and paste. note
#Not creating snapshots as we are in a function which iterates one after the other
    print("Creating snapshot for the volume ...", i["VolumeId"] )
    response = client.create_snapshot(   
        VolumeId=i["VolumeId"]
    )
    #Now after creating snapshot, we want to delete the volume. sometime taking snapshot takes
    #time so we have to delay the next activity by imporitng time. import time under 
    #import boto3 at the begining of the script and delay the next action which is delete below
    time.sleep(5)  #to delay for 5 seconds
    print("Deleting available volumes", i["VolumeId"])
    response = client.delete_volume(
        VolumeId=i["VolumeId"]
    #DryRun=True|False not required... you can take this line off
)
       


