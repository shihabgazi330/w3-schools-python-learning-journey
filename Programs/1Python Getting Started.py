import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
print("Hello Python")

if 5>2:
    print("5 is greater than 2")

x = 5
y = "John"
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x) # this is a string
print(y) # this is an integer
print(z) # this is a float

X, Y, Z = "Orange", "Banana", "Cherry"
print(X)
print(Y)
print(Z)

list1 = ["apple", "banana", "cherry"]
x, y, z = list1
print(x)

x = "awesome"
print(x)

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

def yourfunc():
  global x
  x = "fantastic"

yourfunc()

print("Python is " + x)

x = "Hello World"
print(x.upper())

x = "Hello World"
print(x.lower())

x = "Hello World"
print(x.replace("H", "J"))

x = "Hello World"
print(x.split(" "))

x =  20
print(x,type(x))

x = 20.5
print(x,type(x))

x = 2+1j
print(x,type(x))

x = ["apple", "banana", "cherry"]
print(x,type(x))

x = ("apple", "banana", "cherry")
print(x,type(x))

x = range(6)
print(x,type(x))

x = {"name" : "John", "age" : 36}
print(x,type(x))

x = {"apple", "banana", "cherry"}
print(x,type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x,type(x))

x = True
print(x,type(x))

x = None
print(x,type(x))

x = b'Hello'
print(x,type(x))

x = bytearray(5)
print(x,type(x))

x = memoryview(bytes(5))
print(x,type(x))

x = bytes(5)
print(x,type(x))

c= complex(1,2)
print(c,type(c))

x = object()
print(x,type(x))