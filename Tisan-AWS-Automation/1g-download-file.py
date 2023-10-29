import boto3
s3 = boto3.client('s3')

s3.download_file('tisan-cloud-bucket', 'Kubernetes-Cheat-Sheet.pdf', '/Users/newuser/Desktop/python-introduction/Tisan-AWS-Automation/Kubernetes-Cheat-Sheet.pdf')