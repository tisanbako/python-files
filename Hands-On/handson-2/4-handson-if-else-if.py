marks = 62 #change the marks to give different grades
#max mark 100
if marks >= 85 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks < 85:   #less than 85 to get B ADN EQUAL OR GREATER IS A GRADE
    print("Grade B")
elif marks >= 50 and marks < 75:
    print("Grade C")     
elif marks >=40 and marks < 50:
    print("Grade D") 
else:
    print("Fail")
    print("contact your teacher")      


#we can also use input function    
points = int(input("Enter your points")) #converting the input to int. if you do just the input function, python recognises the numbers as string

if points >= 85 and points <= 100:
    print("Grade A")
elif points >= 75 and points < 85:   #less than 85 to get B ADN EQUAL OR GREATER IS A GRADE
    print("Grade B")
elif points >= 50 and points < 75:
    print("Grade C")     
elif points >=40 and points < 50:
    print("Grade D") 
else:
    print("lose")
    print("train hard")  