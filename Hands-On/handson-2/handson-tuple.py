colors = ("green", "yellow", "red", "yellow")

# colors.append("green") this will show error and tupple is immutable i.e does not let you add or modify it

print(len(colors))
print(colors)
print(type(colors))
print(colors[1])
print(len(colors))

x = colors.count("yellow") #how many times did yellow apear on the list
print(x)
#or just run print(colours.count("yellow")) instead of line 9

x = colors.index("yellow") #i have two yellows.. interesting it picked the first one
print(x)
#or just run print(colours.index("yellow")) instead of line 13


for color in colors: #for loop function
    print(color) #this is to print all the values one after the other. 
#basically color can be anything eg m (for m in colors) color is just a temporary variable
# colors.clear(colors) this wont work as it means we will be modifying the tuple ()   
del(colors) #if we delete, it will delete it from the memory
print(colors) #it will show error cuz it's been deleted
