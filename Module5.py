#List
fruits = ["apple", "banana", "orange"]

print(fruits[1])

fruits[0] = "pear"

print(fruits)

for f in fruits:
    print(f"I love to eat {f.upper()}s")


#tuple
colours = ("red", "yellow", "green")

#cannot do this
# colours.append("blueberry")

#Dictionary
worldFoods = {"Italy": "Pizza", "Spain":"Paella", "American":"BBQ"}
print(worldFoods["Italy"])
worldFoods.update({"France":"Croissant"})
print(worldFoods)

for k in worldFoods.keys():
    print(f"The national dish of {k} is: {worldFoods[k]}")

