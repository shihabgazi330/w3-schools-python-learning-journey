# set the expandtabs to 2 whitespace
txt = "h\te\tl\tl\to"
x = txt.expandtabs(2) # string.expandtab(tabsize)
print(x)
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(3))
print(txt.expandtabs(16))
print(txt.expandtabs(10))
print(txt.expandtabs(-14))