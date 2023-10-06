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
    print(emails2)
    domain = emails2[1]
    domain_name = domain.split(".")
    print(domain_name) #can take off this line.. print is just to see output
    company_name.append(domain_name[0]) #use append function to add company_name to the list
    print(company_name)
   
#we can print all this in one line instead of the many line 13-19
    # company_name.append(i.split("@")[1].split(",")[0])
    # print(company_name)
