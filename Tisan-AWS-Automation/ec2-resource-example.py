import boto3


session = boto3.session.Session(profile_name = "default", region_name = "us-east-1") 

#ec2 = boto3.resource('ec2') if your session is not for default account, ec2 =boto3.resource('ec2') will
#will pick up the default session, instead we mention the session we create

ec2 = session.resource("ec2")
instance = ec2.Instance('id') #which in stance do you want to interact withh