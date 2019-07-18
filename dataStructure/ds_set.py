Days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
Mouths = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 23}
print(Days)
print(Mouths)
print(Dates)

for x in Days:
    print(x)

# Add item to set
Days.add("Reky")
print(Days)

# Remove item from set
Days.discard("Reky")
print(Days)

# Union sets
Days_and_Mouths = Days|Mouths
print(Days_and_Mouths)

#Intersection sets
chooseDays = {"Sun", "Wed", "Dif"}
intersections = chooseDays&Days
print(intersections)

#Difference sets
difference = chooseDays-Days
print(difference)

#Compare sets
subsetRes = Mouths <= Days
supersetRes = Mouths <= Dates
print(subsetRes)
print(supersetRes)