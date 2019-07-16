list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# Access Value in Lists
print("list1 index 0: ", list1[0])
print("list2 print dari index 1 sampai 4: ", list2[1:5])

# Update Value in Lists
list2[0] = 0
print("Update list2 value in index 0 to 0 from 1: ", list2[0])
list3[3] = "e"
print("Add new value to index 3 in list3: ", list3)

# delete value in List
del list2[4]
print("delete value in index 4 in list2: ", list2)
