# Lists are to store multiple items in a single variable.

my_list = ["apple", "banana", "cherry",2 ,4.9, 3j, True, None, ["nested", "list"],(1, 2)]
print(my_list)

# List items are ordered, changeable, and allow duplicate values.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list. important
# Lists are changeable, meaning that we can change, add, and remove items in a list after it has been creaeted.
# Lists allow duplicate values, meaning that two or more items in a list can have the same value.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# List items can be of any data type:
# String, int, float, complex, bool, None, list, tuple etc.

print(type(my_list)) # From Python's perspective, lists are defined as objects with the data type 'list':

# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thislist)

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.