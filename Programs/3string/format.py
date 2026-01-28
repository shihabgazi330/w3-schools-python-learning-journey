# Insert the price inside the placeholder, the peice should be in fixed point, two decimal format.

txt = "for only {price:.2f} dollars"
print(txt.format(price = 49))

# The format() method formats the specified value(s) and insert them inside the string's placeholder. the placeholder is defined using curly brackets: {}.
# The format() method returns the formatted string.
# string.format(val1, val2, ...)

# The placeholder can be identified using named indexes {price}, numbered indedexes{0} or even empty placeholders{}

# Using different placeholder values:

txt1 = "My name is {fname}, I am {age}".format(fname = "Shihab", age = 19)
txt2 = "My name is {0}, I am {1}".format("Shihab", 19)
txt3 = "My name is {}, I am {}".format("Shihab", 19)

print(txt1, "\n"+txt2+"\n"+txt3)


# to demonstrate, we insert the number 8 to set the available space for the value to 8 charecter

# use "<" to left align the value
txt = "We have {:<8} chickens" 
print(txt.format(49))

# use ">" to right align the value
txt = "We have {:>8} chickens"
print(txt.format(49))

# use "^" to center align the value
txt = "We have {:^8} chickens"
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

# use "+" to always indicate if the number is positive or negative
txt = "The temparature is between {:+} and {:+} degrees celcius"
print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

# use a spave ti insert an extra space before positive numbers(and a minus sign before negative numbers)
txt = "The temparature is between {: } and {: } degrees celcius"
print(txt.format(-3, 7))

# use comma as a tohousand separator
txt = "I've {:,} Dollar"
print(txt.format(100000000000000000))

# use underscore as a thousand separator
txt = "I've {:_} Dollar"
print(txt.format(100000000000000000))

# binary format
txt = "binary form of {} is {:b}"
print(txt.format(93438235,93438235))

# converts the value into corresponding unicode charecter
txt = "example: {} to {:c}"
print(txt.format(98,98))

# decimal format
txt = "We have {:d} chickens"
print(txt.format(0b101))

# convert a number into scientific number format
txt = "We have {:e} chickens"
print(txt, "------>", txt.format(5))

# scientific format with an upper case E
txt = "We have {:E} chickens"
print(txt, "------>", txt.format(6))

# fix point number format
txt = "The price is {:.2f} dollars"
print(txt, "------>", txt.format(45))
txt = "The price is {:f} dollars"
print(txt, "------>", txt.format(45))

# Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x = float("inf")
txt = "The price is {:.2F} dollars"
print(txt, "------>", txt.format(x))
x = float("nan")
txt = "The price is {:F} dollars"
print(txt, "------>", txt.format(x))

# general format
txt = "this is a number {:g}"
print(txt, "------>", txt.format(10))
txt = "this is a number {:G}"
print(txt, "------>", txt.format(.1342340))

# octal format
txt = "this is a number {:o}"
print(txt, "------>", txt.format(3284))

# hex format lowear case
txt = "this is a number {:x}"
print(txt, "------>", txt.format(3284))

# HEX format UPPER CASE
txt = "this is a number {:X}"
print(txt, "------>", txt.format(3284))

# number format
txt = "this is a number {:n}"
print(txt, "------>", txt.format(3284))

# percentage format
txt = "this is a number {:%}"
print(txt, "------>", txt.format(3284.8203480923840))

# format map - formats specified values in a string
s = "Assalamualikum, I'm {n1}; are you {n2}"
si = s.format_map({"n1": "Shihab", "n2": "Radia"})

print(si)

txt = "Hello, welcome to my castle"
# searches the steing for a specified value and returns the position of where it was found
print(txt, "------>", txt.index("welcome"))
print(txt, "------>", txt.index("welcome", 5, 15))
# returns true if all charecters in the string are in alphanumeric
print(txt, "------>", txt.isalnum())

# returns true if all charecters in the string are in alphabet
txt = "alphabet"
print(txt, "------>", txt.isalpha()) # txt = "Hello, welcome to my castle" returns fales as it has ','

# returns true if all charecters in the string are in ascii
txt = "alphabeTOJ 10283"
print(txt, "------>", txt.isascii())
# returns true if all charecters in the string are in decimal
txt = "239.2390"
print(txt, "------>", txt.isdecimal())
# returns true if all charecters in the string are in digit
txt = "01010101"
print(txt, "------>", txt.isdigit())

# returns True if the string is a valid identifier, otherwise False. A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a,a.isidentifier())
print(b, b.isidentifier())
print(c, c.isidentifier())
print(d, d.isidentifier())

# returns true if all charecters in the string are in lower case
txt = "alphabeT"
print(txt, "------>", txt.islower())
# returns true if all charecters in the string are in numeric
txt = "3732s"
print(txt, "------>", txt.isnumeric())
# returns true if all charecters in the string are iprintable
txt = "alphabet is a word \n \bI\'m using that"
print(txt, "------>", txt.isalnum())
# returns true if all charecters in the string are space
txt = "      "
print(txt, "------>", txt.isalnum())
# Returns True if the string follows the rules of a title

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a,a.istitle())
print(b, b.istitle())
print(c, c.istitle())
print(d, d.istitle())

# returns true if all charecters in the string are in uppercas
txt = "ALPHABET"
print(txt, txt.isalnum())

# joins the elements of an iterable to the end of the string
tup = ("Shihab", "Radia", "Jihad")
print(tup, "#".join(tup))

# Returns a left trim version of the string
print("banana".ljust(20), "is my favourite food")

# returns a translation table to be used in translations
txt = "Assalamualaikum, Shihab!"
MyTable = str.maketrans("S", "P")
print(txt, txt.translate(MyTable))
# the maketrans() method returns a mapping table that can be used with the translate() mthod to replace specified characters
# str.maketrans(x, y, z)
x = "mSa"
y = "eJo"
z = "Assalamualaikum"
# MyTable = str.maketrans(x)
# print(txt, txt.translate(MyTable)) give error
MyTable = str.maketrans(x, y)
print(txt, txt.translate(MyTable))
MyTable = str.maketrans(x, y, z)
print(txt, txt.translate(MyTable))

# the method maketrns itself returns a dictionary describing each replacement, in unicode
print(str.maketrans(x,y,z))

# partition() returns a tuple where a string is parted into 3 parts centering the specified value with it's first occurance
txt = "my name is shihab gazi"
print(txt.partition("shihab"))
print(txt.partition("a")) # a is repeated several times
print(txt.partition("banana")) # if the string is not found then the partition method gives us a tuple with 3 elements, the whole string, an empty element and another empty element

# returns a string where a specified value is replaced with a specified value
print(txt.replace("my", "your"))
print(txt.replace("a", "o"))
print(txt.replace("a", "o", 2)) # also defines the occurances. the default is all occurance


# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Hello, welcome to my castle."
x = txt.rfind("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
# print(txt.rindex("q")) raises an error
# swapes cases, lower case becomes upper case and vice versa
print(txt.swapcase())

# returns a right justified version of the string
print(txt.rjust(30))
print(txt.rjust(30, "0"))
print(txt.rjust(-4, "o"))

# converting the first charecter of each of the word of the string into uppercase
print(txt.title())

# rpartition() returns a tuple where a string is parted into 3 parts centering the specified value with it's last occurance
txt = "my name is shihab gazi"
print(txt.rpartition("shihab"))
print(txt.rpartition("a")) # a is repeated several times
print(txt.rpartition("banana")) # if the string is not found then the rpartition method gives us a tuple with 3 elements, an empty element, another empty element and the whole string

# Splits the string at the specified separator, and returns a list
# string.rsplit(separator, maxsplit)
txt = "apple, banana, cherry, pineapple, jackfruit, orage, malta"
x = txt.rsplit(", ")
print(x)
txt = "apple, banana, cherry, pineapple, jackfruit, orage, malta"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

# Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
# string.rstrip(characters)
# Remove the trailing characters if they are commas, periods, s, q, or w:

# txt = "bana,,,,,ssqqnqww....na"
# x = txt.rstrip(",.qsw")
# print(x) won't work

# split()	Splits the string at the specified separator, and returns a list just like rsplit

# Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

txt = "Thank you for the music\nWelcome to the jungle"
# Split a string into a list where each line is a list item:
x = txt.splitlines()
print(x)
# Split the string, but keep the line breaks:
x = txt.splitlines(True)
print(x)

# Check if position 7 to 20 starts with the characters "wel":
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)