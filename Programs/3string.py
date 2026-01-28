# STRINGS
# txt = input("Enter your text here: ")

# x = input("Search for the word: ")

# print(f"Length of your text is {len(txt)}")
# print(x.lower() in txt.lower())
# print("Shihab".lower() not in txt.lower())



# SLICING STRINGS
b = "Hello my World"
print(b[:5]) # by leaving out the first index, the range will start at the first character

print(b[2:]) # leaving out characters until position 2, and all the way to the end:

# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
print(b[-5:-2]) # Use negative indexes to start the slice from the end of the string:



# MODIFY STRINGS
print(b.upper())
print(b.lower())
space = "		Shihab Gazi		"
print(f"space varible with space {space} and without space {space.strip()}") # the strip() method removes any whitespace from the begging or the end
print(space.replace("Shihab", "Radia")) # replace(	) method replaces a string with another string
print(b.split(",")) # the split method returns a list where the text between the specified separator becomes the list items. It splits the string into substrings if it finds instances of the separator.



# MARGING VARIABLES
c = b + space
print(c)



# ESCAPE CHARACTERS
print("there are many escape characters such as: \", \\, \n i.e. \\n, \t, Hello\rWorld, Hello \bWorld, \f, \x48\x65\x6c\x6c\x6f and",'\'')
print("Result in octal value \110\145\154\154\157")
print("Result in hexadecimal value \x48\x65\x6c\x6c\x6f")




# STRINT METHODS

print(f"""
{b.capitalize()}capitalize()	Converts the first character to upper case
{b.casefold()}casefold()	Converts string into lower case
{b.center(20,"0")}center()	Returns a centered string
{b.count('l')}count()	Returns the number of times a specified value occurs in a string
{b.encode()}encode()	Returns an encoded version of the string
{b.endswith('d')}endswith()	Returns true if the string ends with the specified value
{b.expandtabs()}expandtabs()	Sets the tab size of the string
{b.find('o')}find()	Searches the string for a specified value and returns the position of where it was found
{b.format()}format()	Formats specified values in a string
{b.format_map(dict())}format_map()	Formats specified values in a string
{b.index('o')}index()	Searches the string for a specified value and returns the position of where it was found
{b.isalnum()}isalnum()	Returns True if all characters in the string are alphanumeric
{b.isalpha()}isalpha()	Returns True if all characters in the string are in the alphabet
{b.isascii()}isascii()	Returns True if all characters in the string are ascii characters
{b.isdecimal()}isdecimal()	Returns True if all characters in the string are decimals
{b.isdigit()}isdigit()	Returns True if all characters in the string are digits
{b.isidentifier()}isidentifier()	Returns True if the string is an identifier
{b.islower()}islower()	Returns True if all characters in the string are lower case
{b.isnumeric()}isnumeric()	Returns True if all characters in the string are numeric
{b.isprintable()}isprintable()	Returns True if all characters in the string are printable
{b.isspace()}isspace()	Returns True if all characters in the string are whitespaces
{b.istitle()}istitle()	Returns True if the string follows the rules of a title
{b.isupper()}isupper()	Returns True if all characters in the string are upper case
{'-'.join(['a','b','c'])}join()	Joins the elements of an iterable to the end of the string
{b.ljust(20)}ljust()	Returns a left justified version of the string
{b.lower()}lower()	Converts a string into lower case
{b.lstrip()}lstrip()	Returns a left trim version of the string
{str.maketrans('abc', '123')}maketrans()	Returns a translation table to be used in translations
{b.partition(' ')}partition()	Returns a tuple where the string is parted into three parts
{b.replace('Hello', 'Hi')}replace()	Returns a string where a specified value is replaced with a specified value
{b.rfind('o')}rfind()	Searches the string for a specified value and returns the last position of where it was found
{b.rindex('o')}rindex()	Searches the string for a specified value and returns the last position of where it was found
{b.rjust(20)}rjust()	Returns a right justified version of the string
{b.rpartition(' ')}rpartition()	Returns a tuple where the string is parted into three parts
{b.rsplit()}rsplit()	Splits the string at the specified separator, and returns a list
{b.rstrip()}rstrip()	Returns a right trim version of the string
{b.split()}split()	Splits the string at the specified separator, and returns a list
{b.splitlines()}splitlines()	Splits the string at line breaks and returns a list
{b.startswith('H')}startswith()	Returns true if the string starts with the specified value
{b.strip()}strip()	Returns a trimmed version of the string
{b.swapcase()}swapcase()	Swaps cases, lower case becomes upper case and vice versa
{b.title()}title()	Converts the first character of each word to upper case
{b.translate(str.maketrans('e', '3'))}translate()	Returns a translated string
{b.upper()}upper()	Converts a string into upper case
{b.zfill(20)}zfill()	Fills the string with a specified number of 0 values at the beginning""")



























