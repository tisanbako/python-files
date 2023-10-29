import boto3
import time  #because we need to back up the volume before we delete and we need a delay 
#the delete execution while creating snapshot before deleting

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
print(len(response["Volumes"]))
for i in (response["Volumes"]):
    print(i["VolumeId"])  #now that you have identified the two volumes, create snampshot
    print("creating snap shots......")
    response = client.create_snapshot(
        VolumeId= i["VolumeId"]
)
    time.sleep(5)    #delay for 5 seconds
    print("Deleting Volumes")
    response = client.delete_volume(
        VolumeId= i["VolumeId"]
    
)
