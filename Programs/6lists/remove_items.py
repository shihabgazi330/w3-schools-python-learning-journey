machines = ["Laptop", "Mobile", "Fan", "Light", "TV", "Mobile", "Reftrigerator", "Air Conditionar", "Mobile", "Router"]
print(machines)

# The remove() method removes the specified item.
machines.remove("Mobile")
print(machines) # the remove() method removes only the first occurrence

# removes the specified index
machines.pop(3)
print(machines)
machines.pop(-3) # removes the last 3rd item
print(machines)
machines.pop() # remove the last item
print(machines)

# removing a specific index item
del machines[3]
print(machines)

# del keyword can also delete the list compeletely
temporary_list = [1,2,4,5,"", True]
del temporary_list
# print(temporary_list) raises an error

# making a list empty, the list itself remains
machines.clear()
print(machines, type(machines)) # no error just an empty list