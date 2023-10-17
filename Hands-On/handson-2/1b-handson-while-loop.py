#password simulation.. say you want a user to only try to log in with
#wrong password 4 times

correct_pin = 1234
wrong_attempt = 0
while wrong_attempt <4:
    entered_pin = int(input("what is yout pin: "))     #conver it to int cuz for loop see's everything as str
    if entered_pin == correct_pin:
        print("logging you in now!")
        break   #if the pin is correct or else attempt whatever time like below
    wrong_attempt += 1


