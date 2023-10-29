import boto3

client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=[
        'i-020f877852d48ee44',
    ],
)

print(response)