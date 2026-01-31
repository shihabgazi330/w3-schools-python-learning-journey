# for sorting the items of a list we have a method named sort()

fruits = ["apple", "avcado", "jackfruit", "pineapple", "mango", "banana", "kiwi", "cherry", "almonds"]
fruits.sort()
print(fruits)

nums = [4,2,5.25,3,19,5,3]
nums.sort()
print(nums)

# to sort items in reverse
fruits.sort(reverse=True)  # this will sort in reverse (in place)
print(fruits)  # this will print the sorted list
nums.sort(reverse=True)
print(nums)

# CUSTOMIZE SORT FUNCTION

# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)

this_list = [100, 50, 85,392, 40000,293,.32,43,2,2396857362j]
this_list.sort(key = myfunc) # customizing the sort method using my own function
print(this_list)

# CASE INSENSITIVE SORT
# by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
new_list = ["shihab","Shihab","shiHab", "banana", "Orange", "Kiwi", "cherry"]
new_list.sort() # case sensitive sorting can give an unexpected result
print(new_list)

new_list.sort(key = str.lower) # using built in function as key function to sort the list
print(new_list)

# REVERSE ORDER
lets_say = "my name is shihab"
list_from_lets_say = lets_say.split()
print(list_from_lets_say)
list_from_lets_say.reverse()
print(list_from_lets_say)
print(list)

if lets_say.split() == [i for i in lets_say.split()]:
    print("No Problem")