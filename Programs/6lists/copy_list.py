# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

fruits = ["apple", "avcado", "jackfruit", "pineapple", "mango", "banana", "kiwi", "cherry", "almonds"]
# copying using copy method
CopyOfTheList = fruits.copy()
print(CopyOfTheList)
shihab = ["banana", "Orange", "Kiwi", "cherry"]
# copying using list method
CopyOfTheList = list(shihab)
print(CopyOfTheList)

# copying using : OPERATOR
from datetime import date
today = date.today()
year = today.year
items = [x for x in range(year+1)]

CopyOfTheList = items[:]
print(CopyOfTheList)
if list(shihab) == shihab.copy() and shihab[:]:
    print("no problem".title())
else:
    print("raises an error".title())
