groceries = {"eggs", "milk", "veggies", "fruits", "eggs"}

print(groceries) #it will print with only one egg. no duplicate

movies = {"wakanda", "spiderman", "hulk", "ironman", "hulk"}
print(movies)
#print(movies[0]) this will throw error as no indexing.. we can use for loop function if we want to access what is inside the set

#set does not use indexing, as it does not care about sequencing hence we cannot
#access the individual indexing
#if we want to access it one after the other, we use "for loop"

movies = {"wakanda", "spiderman", "hulk", "ironman", "hulk"}

movies.add("ariel") #Adds an element to the set
print(movies)

movies2 = {"safafina", "wakanda", "karashika", "hulk", "nneka"}

fav_movies = movies2.difference(movies)
print(fav_movies)

fav_movie2 =movies2.intersection(movies)
print(fav_movie2)
