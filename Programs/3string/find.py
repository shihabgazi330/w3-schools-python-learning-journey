txt = "Hello, welcome to my castle"
print(txt.find("welcome"))

# the find() method finds the first occurance of the specified value and returns -1 if the value is not found
# it's almost same as the index() method, with only exception being index() method raises an exception if the value is not found

# string.find(value, start, end)

txt.find("e", 5, 10)

print(txt.find("q"))
print(txt.index("q"))