#Suppose your exam marks in various subjects are stores like this 

#marks = [55,64,75,80,65]

#how do you 
#1. Find the average marks you obtain from the exam, and based on the average marks
#you want to find your grade. The grading rule is like this 

# A if the average marks is equal to or above 80
# B if the average mark is equal to 60 and less than 80
# c if the average mark is equal to 50 and less than 60
#And ifthe average marks is less than 50, you will get Grade F


# def finding_average_mark(mark):
#     average_mark = sum(mark)/len(mark)
#     return average_mark



# marks = [55,64,75,80,65]
# print(finding_average_mark(marks))

#now we have found the average... inside the average function, we need to create
#the grade function

def finding_average_mark(mark):
    # average_mark = sum(mark)/len(mark)
    # sum_mark = sum(mark)
    # length_marks = len(mark)
    # average_mark = sum_mark/length_marks
    average_mark = sum(mark)/len(mark)
    return average_mark

def finding_grade(average_mark):
    if average_mark >= 80:
        grade = "A"
    elif average_mark  >= 60 and average_mark <= 80:
        grade = "B"
    elif average_mark  >= 50 and average_mark <= 60: 
        grade = "C"
    else:
        grade = "D"      
    return grade    

tisan_marks = [55,64,75,80,65]
average_m = finding_average_mark(tisan_marks)
print(average_m)

grade = finding_grade(average_m)
print("your grade is", grade)
