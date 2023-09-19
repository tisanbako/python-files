emails = ["ironman@accenture.com", 
          "naruto@netflix.com",
          "toni@insta.org",
          "hulk@ey.com",
            "blackpanta@microsoft.in"
            ]
#to access an email we use index, to access all emails one at a time we use loop function

for i in emails:  #i could be anything 
    print(i)
    emails2 = i.split("@") #this will apply for all emails as for loop function works on one email at a time 
    print(emails2)
    domain = emails2[1]
    print(domain)
    domain_name = domain.split(".")
    print(domain_name)
    company_name = domain_name[0]
    print(company_name)

















    # emails3 = emails2[1]
    # print(emails3)
    # emails4 = emails3.split(".")
    # print (emails4)
    # company_name = emails4[0]
    # print(company_name)