fruits = ["kiwi", "apple", "grapes", "mangos", "watermelon", "oraages"]

for i in fruits:
    print(i)     #this is to iterate the whole list
    if i == "grapes": 
        print("found the fruit we have been looking for") #in the if block, but it keeps iterating

#it will print         
# kiwi
# apple
# grapes
# found the fruit we have been looking for
# mangos
# watermelon
# oraages

#what is we want the look to stop after it grape?
fruits2 = ["kiwi", "apple", "grapes", "mangos", "watermelon", "oraages"]

for a in fruits2:
    print(a)     #this is to iterate the whole list
    if a == "grapes": 
        print("found the fruit we have been looking for") 
        break

#print
# kiwi
# apple
# grapes
# found the fruit we have been looking for    


        
