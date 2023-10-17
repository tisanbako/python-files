#FOR LOOP - to iterate over sequence of collcetion of items (tupple, str, list, set)
#while loop - to interate when condition is true. while something exist keeo looping

count = 0

while count <5:

    print("infinity")  #crt c to stop
    #use break to stop it or use a statement to stop it eg below
    count = count + 1  #everytime it iterates value of count increaes by 1

#password simulation.. say you want a user to only try to log in with
#wrong password 4 times

correct_pin = 1234
wrong_attempt = 0
while wrong_attempt <4:
    entered_pin = input("what is yout pin: ")
    if entered_pin == correct_pin:
        print("logging you in now!")
        break   #if the pin is correct or else attempt whatever time like below
    wrong_attempt += 1


#Lets say we want our battery to show "low battery" if it's less than 15 percent
current_battery_percentage = int(input("Enter current battery percentage: "))
while current_battery_percentage <15:
    print("LOW BATTERY!!")
    current_battery_percentage = current_battery_percentage + 1  #SAY YOU'RE CHARGING YOU PHONE, IT'LL KEET INCREASING % BY %
    