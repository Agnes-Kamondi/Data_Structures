# Sample code in Python
arr = [1, 2, 3, 4, 5,6,7,8,9,10]
print(arr.count(3))

#checking the length
len(arr)

#traversal
for x in arr:
 print(x)

# Access
print(arr[2]) 

# Insertion
#one value
arr.append(11)
print(arr)
arr.append(12)
#a list or any other iteration
arr.extend([13,14,12,2]) 
#inserting a value at a specific index
arr.insert(1,20)
arr.append(1)
#checking the first occurence of something in a list
print(arr.index(2))

# Deletion
#using index
del arr[3]
#removing the last index
arr.pop()
print(arr)
#removing when specifying the item you are removing
arr.remove(1) #removes the first occurrence of the specified number like in our example the remove method will remove just one 1
print(arr)

# Search
if 4 in arr:
 print("Found")
else:
 print("not found")

#reversing an array
 arr.reverse()
 print(arr)

#sorting an array
 arr.sort()
 print(arr)


