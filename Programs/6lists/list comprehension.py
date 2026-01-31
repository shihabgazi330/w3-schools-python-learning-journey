# list comprehension provides a shorter syntex to create a new list based on the values of an existing list
# for example based on the list of fruits I want a new list containing only the fruits with the letter "p" the name.
# without list comprehension I have to write a for statement with a conditional test inside:

fruits = ["apple", "avcado", "jackfruit", "pineapple", "mango", "banana", "kiwi", "cherry", "almonds"]
new_list = []
print("the list:".capitalize, fruits)
# usig for loop the long way
for x in fruits:
    if "p" in x:
        new_list.append(x)

print(new_list)

# using list comprehension the shorter way
new_list1 = [x for x in fruits if "p" in x]
print(new_list1)

# syntex: newlist = [expression for item in iteravle if condition == True]
# the return value is a new list, leaving the old list unchanged.

# CONDITION: the condition is like a forlter trhat only accepts the items that evaluate to True.
# Only accept items that are not "apple"

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# the condition if x != "apple" will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# the condition is optional and can be omitted:
newlist = [x for x in fruits]
print(newlist)

# ITERABLE: the iterable can be any iterable object, like a list, tuple, set etc.
# using range() function to create an iterable:
numlist = [x for x in range(10)]
print(numlist)

# same example but with an condition
numlist = [x for x in range(10) if x < 5]
print(numlist)

# setting the values in the new list to upper case:
speacial_list = [x.upper() for x in fruits]
print(speacial_list)

# setting all values in the new list to "hello"
speacial_list = ["hello" for x in fruits]
print(speacial_list)

# returning "orange".title() istead of banana
speacial_list = [x if x != "banana" else "orange".title() for x in fruits]
print(speacial_list)

# applying .title() function on each item of the fruits list
titled_fruits = [item.title() for item in fruits]
print(titled_fruits)

# titled_fruits[i] = fruits[i].title() this is not right aproach
# print(titled_fruits) this is not right aproach

# modifying the same list in place (not always possible)
fruits[:] = [item.title() for item in fruits]
print(fruits)

# for mixed list
mixed = [1,1,2,3,4, True, speacial_list, numlist, "shihab", "chair", "AC"]
# applying condition
# mixed[:] = [item.title() for item in mixed] # raises an error
mixed[:] = [item.title() if isinstance(item, str) else item for item in mixed]
print(mixed)

mixed[:] = [[x.title() if isinstance(x, str) else x for x in item]
            if isinstance(item, list)
            else item.title() 
            if isinstance(item, str)
            else item
            for item in mixed
            ]
print(mixed)

# the same code as above but in one line
mixed[:] = [[x.title() if isinstance(x, str) else x for x in item] if isinstance(item, list) else item.title() if isinstance(item, str) else item for item in mixed]
print(mixed)
