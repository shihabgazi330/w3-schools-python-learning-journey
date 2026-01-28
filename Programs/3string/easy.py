# go and view https://www.w3schools.com/python/python_ref_string.asp

txt = "my name is shihab" 

print(txt.capitalize(), "->capitalize")
print(txt.upper(), "->upper")
print(txt.lower(), "->lower")
print(txt.casefold(), "->casefold")
print(txt.center(30), "->center")
print(txt.center(30, "0"), "->center()")
print(txt.count("shihab"), "->count")
print(txt.count("shihab", 10, 30), "->count")
print(txt.encode())

age = 16

txt = f"My name is Shihab and I'm {age}"
print(txt)

price = 30
txt = f"The price is {price:.3f} Taka"
print(txt)