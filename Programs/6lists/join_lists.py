shihab = ["banana", "Orange", "Kiwi", "cherry"]
fruits = ["apple", "avcado", "jackfruit", "pineapple", "mango", "banana", "kiwi", "cherry", "almonds"]

# joining two lists and saving them into a new variable
joined_list = shihab+fruits
print(joined_list)

# joining two lists and saving them into one of them
for x in fruits:
    shihab.append(x)
print(shihab)

# super simple way
nums = [x for x in range(8)]
fruits.extend(nums)
print(fruits)

for _ in fruits:
    shihab.append(fruits) # not a right way
print(shihab)

#############