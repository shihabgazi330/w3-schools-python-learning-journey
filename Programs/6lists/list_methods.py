# Add an element to the fruits list:

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange") # An element of any type (string, number, object etc.)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
c = b.copy()
b.clear()
print(b)

print(fruits.count("cherry")) # Any type (string, number, list, tuple, etc.). The value to search for.

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

c = []
c.extend(points + fruits)
print(c)
# print(c.index("shihab")) raises an error as "shihab" is not an item of c
print(c.index("apple"), c.index(9))
x = c.index(9, 4) # find the position of 9 but start the search at position 4
# x = c.index(2, 4) raises an error
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange") # list.insert(pos, elmnt)
print(fruits)
fruits.pop(1)
print(fruits) # list.pop(pos)

# Return the removed element:
x = fruits.pop(1)
print(x)
print(fruits)

# fruits.remove("banana") # raises an error as "banana" is no more in the fruits list
c.remove("banana") # as I have exteded c to fruits list and points list the remove method applied on fruits list doesn't affect the list c
# although x = fruits.pop(1) would affect c if I had writen c = fruits + points
print(c)

print(fruits.reverse())
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort() # list.sort(reverse=True|False, key=myFunc)
print(cars)

cars.sort(reverse=True)
print(cars)

# A function that returns the length of the value:
def myFunc(e):
    return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

# A function that returns the 'year' value:
def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

# A function that returns the length of the value:
def myFunc(e):
    return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)