# Membership operators are used to test if a sequence is presented in an object:

# Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

# The membership operators also work with strings:
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)