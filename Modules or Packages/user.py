from AWS import rds
from AWS import s3  #we could also say from AWS import rds,s3

rds.insert_user_info("ironman", "ironman@wakanda.com", "admin123")
s3.upload_profile_pic()