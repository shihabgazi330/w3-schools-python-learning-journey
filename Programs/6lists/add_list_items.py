# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#  insert a list item at a specified index
thislist.insert(3, "pineapple")

# append elements from another list
names = ["Mohammad", "Ali", "Shihab"]
nums = [1,2,3,4,5,6,7]
names.extend(thislist+ nums)
print(names)

# appending tuples, sets, dictionaries.....
this_tuple = ("tuple", 13,35,12, "tuple")
set0 = {1,2,4,5,3,5,"",4,3,4,45}
dict0 = {"name" : "shihab", "universiy" : "SUST"}
# names.extend(this_tuple+set0+dict0) # will raise an error
# names.extend(this_tuple,set0,dict0) # will raise an error

# NO PROBLEM!
names.extend(this_tuple)
print(names)
names.extend(set0)
print(names)
names.extend(dict0)
print(names)