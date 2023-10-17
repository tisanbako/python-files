#continue is to stkip an iteration.
#break stops the for loop iteration for that point while.
#lets say we want to skip grapes from below list

fruits = ["kiwi", "apple", "grapes", "mangos", "watermelon", "oranges"]

for i in fruits:
    if i == "grapes":
        continue
    print("adding to favorite fruits:", i)


fruits2 = ["sour_soup", "pineapple", "tiger-fruit", "lemon", "grapes", "cashew"]

for a in fruits2:
    if a == "grapes" or a == "cashew" :
        continue
    print("adding to favorite fruits:", a)
