name = "tisan"
company = "emstereb"

print(len(name))
print("a" in name) #is a letter in the word tisan 
print(name[1])

#dir() functions for string () is in the function for string
print(name.upper())
print(name.capitalize())
print(company.replace("reb", "Reb Services")) #change reb in emstereb to Reb and add Services


username = "   tisanb   "
print(len(username)) #this will say 12 instad of 5 due to the spaces and this will eat your memory
#best thing to do us use the functions lstrip (take out left space), rstrip (right space), strip (take off all spaces)
proper_username = username.strip()
print(len(proper_username))

message = "hello, everyone, how is it going"
print(message.split()) #['hello,', 'everyone,', 'how', 'is', 'it', 'going'].... split Splits the string at the specified separator, and returns a list
print(message.split(",")) #['hello', ' everyone', ' how is it going']

email = "bakotisan@gmail.com"
print(email.split("@")) #['bakotisan', 'gmail.com']
print(email.split("n")) #['bakotisa', '@gmail.com']