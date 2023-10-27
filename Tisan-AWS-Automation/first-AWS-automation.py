import boto3


session = boto3.session.Session(profile_name = "default", region_name = "us-east-1") #profile name could be from any account