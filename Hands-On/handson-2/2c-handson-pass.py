#pass is like passing control to someone. it is like a place holder for functions
#for example when you use the for loop, if statement or while loop
# for i in fruits:       #definately some lines of code is suppose to come under this function
#but if we don't have the implimentation for the time being and we want the python in
#interpreter to not show us error, we use pass below eg

for i in range(4):
    pass       #if i run this code without the pass keyword, it will show me an error cuz something is suppose to be under the loop







print("tisan")

def get_db_secrets():      #say we don't have where to get the secret at this moment
    pass     #remove pass and it will show error 