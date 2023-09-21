#Task - if any email is from accenture or ey, send partner coupon code 
#with 70% off else sprint sending coupon code with 10%
#First we start by looking at where we have all the emails in a loop and that is 
# On line ** (for i in emails: ) here all the emails are on a look in "i" 
#you look for the email cuz you will need it for the emails that will get 10% or 70% coupon
#Second you need to know where the companies names are also for thesame reason as 
#the criteria is for emails from "accenture" and "ey" and that is on line
#

emails = ["ironman@accenture.com", 
          "naruto@netflix.com",
          "toni@insta.org",
          "hulk@ey.com",
          "blackpanta@microsoft.in"
          ]

company_name = []

for i in emails:  #i could be anything 
    print(i)
    emails2 = i.split("@") #this will apply for all emails as for loop function works on one email at a time 
    print(emails2)
    domain = emails2[1]
    domain_name = domain.split(".")
    print(domain_name) #can take off this line.. print is just to see output
    company_name.append(domain_name[0])#use append function to add all company_name to the list of loops
    #to check for the emails with the name accenture and ey we use the if functiom
    if company_name == "accenture" or domain_name[0] == "ey":
        print("sending partner coupon code with 70% to email " , i) # i the loop in i for where we fot the email (for i in emails:))
    else:
        print("sending coupon code with 10% discount to email ", i)    
              


