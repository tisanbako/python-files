
#want to stop all running instances with the tags 'dev',  and 'test'
#create three instances with tags dev, prod, test

import boto3

client = boto3.client('ec2')

response = client.describe_instances(  #go to the doc and copy the filter part
    Filters=[
        {
            'Name': 'tag:env',
            'Values': [
                'dev', 'test',
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values': [
                'running'
            ]
        },
    ],
)
for i in response["Reservations"][0]["Instances"]:    #you need to have a running instance if not it will say out of range
    print(i)
    print()
    # now write the module to stop instance.. go check the doc
    response = client.stop_instances(
    InstanceIds=[
        i["InstanceId"]
    ],
    )




# response = client.describe_instances()

# response.keys()                #dict_keys(['Reservations', 'ResponseMetadata'])
# # print(response.keys())   #this will print dict_keys(['Reservations', 'ResponseMetadata'])
# print(len(response["Reservations"]))
# print(type(response["Reservations"]))  #reservation is a list while ResponseMetadata is dict

# #if you check the documentation, there are group and instances in the list under reservation
# #we want to check details of instances
# print(response["Reservations"][0]["Instances"]) #["Reservations"][0] is cuz at the time i created the instances i created them just once and only have 1 reservation, so the indexwould be 0
# #lets's try to get instance id

# for i in response["Reservations"][0]["Instances"]:
#     print(i["InstanceId"])



