tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = ()
tup5 = (50, )

print("Berikut adalah value dari tup1 index 0: ")
print(tup1[0])
print("Berikut adalah value dari tup3 keseluruhan:")
print(tup2)

#create new tuple using concat variable
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2
print("\n Berikut adalah hasil concat dari existing variable name")
print(tup3)

#delete value list (not possible, will get error
del tup1[4]
print("Delete value from variable list tup1 in index 4: ", tup1)
