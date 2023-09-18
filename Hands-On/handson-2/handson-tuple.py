colors = ("green", "yellow", "red", "yellow")

# colors.append("green") this will show error and tupple does not let you add or modify it

print(colors)
print(type(colors))
print(colors[1])
print(len(colors))
x = colors.count("yellow")
print(x)

x = colors.index("yellow") #i have two yellows.. interesting it picked the first one
print(x)

for color in colors:
    print(color)

# colors.clear(colors) this wont work as it means we will be modifying the tuple ()   
del(colors) #if we delete, it will delete it from the memory
print(colors) #it will show error cuz it's been deleted
