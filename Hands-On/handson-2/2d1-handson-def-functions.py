#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

def tisan_function(): 
    print("hello from the other side")

#the print in the body of the function will not print. to bring a function to action, 
# we need to call the function  
#To call a function, use the function name followed by parenthesis:

def tisan_function(): 
    print("hello from the other side")

tisan_function()    

#RETURN


#A function can also beis used to avoid repitition to create reusable codes
#by calling it multiple time. they can have different values as you call them

def get_secrets_from_ssm():
    print("connecting to secret manager, getting user-db-credentials")
    print("connecting to AWS dev env")
    print("got the credentials")
    print("closing the connection to aws")

get_secrets_from_ssm()   #to print once    
get_secrets_from_ssm()    #to print twice
get_secrets_from_ssm()    #to print three times

#here every print statement will be printed three times as we called it 3 times

    #ARUMENTS
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.

def bako_function(name, surname):
    print("my names are ", name, surname)

bako_function("Jeremiah", "Bako")
bako_function("samuel", "Johnson")    
    

#EX3    
def arithmentics_ops(no1, no2):
    result = (no1 + no2)
    print(result)

arithmentics_ops(2, 3)       


#eX3
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# #as you can see in the above example. lets say we have three database for three different 
# #micro-service. and we want to write code for connecting to them. all three script 
# #have same key, may be different values. now to seperate the script for the different 
# #mictoservice we name them on the get_secret_from_ssm("")
# #then on the second print above we need to may the credential we are getting dynamic


def get_secrets_from_ssm(secret_name):
    print("connecting to secret manager, getting", secret_name)
    # print("connecting to AWS dev env")
    # print("got the credentials")
    # print("closing the connection to aws")

get_secrets_from_ssm("user_db-secret")      
get_secrets_from_ssm("movie-db-secret")   
get_secrets_from_ssm("payments-db-secret")   

