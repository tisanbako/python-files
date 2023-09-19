emails = ["ironman@accenture.com", 
          "naruto@netflix.com",
          "toni@insta.org",
          "hulk@ey.com",
            "blackpanta@microsoft.in"
            ]
#to access an email we use index, to access all emails one at a time we use loop function

#lets say we are looking for the value of company names from the emails above
company_name = []

for i in emails:  #i could be anything 
    print(i)
    emails2 = i.split("@") #this will apply for all emails as for loop function works on one email at a time 
    domain = emails2[1]
    domain_name = domain.split(".")
    print(domain_name) #can take off this line.. print is just to see output
    company_name = domain_name[0]
    print(company_name)

#the print lines not necessary















    # emails3 = emails2[1]
    # print(emails3)
    # emails4 = emails3.split(".")
    # print (emails4)
    # company_name = emails4[0]
    # print(company_name)