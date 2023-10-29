import boto3

client = boto3.client('s3')

client.upload_file('/Users/newuser/Desktop/python-introduction/Tisan-AWS-Automation/1g-story.txt', 'tisan-cloud-bucket', '1g-story.txt')
#                                 #total path of the file                     #the s3 bucket                          #name of the file


#to get the full path right click the file - copy path