import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.describe_instances(  
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
        ]
    )
    print("instances information with given criteria: ", response)
    for i in response["Reservations"][0]["Instances"]:
        print("stopping instance with id: ", i["InstanceId"])
        response = client.start_instances(
        InstanceIds=[
            i["InstanceId"]
        ],
        )
      