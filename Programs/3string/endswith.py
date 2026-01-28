# Check if the string ends with a punctuation sign (.):

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# The endswith() method returns True if the string ends with the specified value, otherwise False.
# SYNTEX
# string.endswith("value", start, end)
# value - RECQUIRED. The value to check if the string ends with. This value parameter can also be a tuple, then the method returns true if the string ends with any of the tuple values.
# start - OPTIONAL. An integer specifying at which position to start the search.
# end - OPTIONAL. An integer specifying at which position to end the search.

# CHECK IF THE POSITION 5 TO 11 endswith the phrase "my world":
txt = "Hello, welcome to my world"
x = txt.endswith("my world", 5, 11)
print(x)

# CHECK IF THE string endswith either the phrase "castle" or "world":
txt = "Hello, welcome to my castle"
x = txt.endswith(("castle", "world"))
print(x)

