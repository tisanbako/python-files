email = "tisan.bako@bellmedia.ca"
new_email = email.split("@") #store "['tisan.bako', 'bellmedia.ca']" in a variable new_email
print(new_email)  #['tisan.bako', 'bellmedia.ca']
print(new_email[0]) #tisan.bako
print(type(new_email[1]))  #<class 'str'>

#to futher seprate new_email = bellmedia.ca[1]

email2 = new_email[1]  #store "bellmedia.ca" in a variable
print(email2)

email3 = email2.split(".")
print(email3) #['bellmedia', 'ca']

company_name =email3[0]
print(company_name)  #bellmedia

#we can achieve all that with this one line 
# print(email.split("@")[1].split(".")[0])