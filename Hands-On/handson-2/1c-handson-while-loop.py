
#Lets say we want our battery to show "low battery" if it's less than 15 percent
current_battery_percentage = int(input("Enter current battery percentage: "))
while current_battery_percentage <15:
    print("LOW BATTERY!!")
    current_battery_percentage = current_battery_percentage + 1  #SAY YOU'RE CHARGING YOU PHONE, IT'LL KEET INCREASING % BY %
