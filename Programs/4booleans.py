# booleans represent one of two values: True or False

print(10>9)
print(10==9)
print(10<9)

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if (a>b):
    print(f"the first number a i.e. {a} is grater than b i.e {b}")
else:
    print(f"the first number a i.e. {a} is not grater than b i.e {b}")

# THE bool function allows you to evaluate any value and give you True or False in return
print(bool(15)) # in python any non zero number is True
print(bool("Hello")) # in python any non empty string is True

# these returns False
print(0, bool(0))
print("", bool(""))
print([], bool([]))
print({}, bool({}))
print(None, bool(None))
print((), bool(()))
print(False,bool(False))

name = "Shihab"

if name: # no need to write if name != ""
    print("Name exists")

# isinstance() function, which can be used to determine if an object is of a certain data type:
x = 19 + 23j
print(isinstance(x, float))
print(isinstance(x, str))
print(isinstance(x, int))
print(isinstance(x, complex))
print(isinstance(x, set))
print(isinstance(x, dict))
print(isinstance(x, tuple))

# w3 schools also teaches about class, function about which I'm still not familiar enough to learn so I am skipping this part for a while. So the file is uncompelete for a while