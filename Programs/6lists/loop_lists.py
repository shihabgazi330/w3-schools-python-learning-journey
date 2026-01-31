# using loops we can print out list items one by one at the same time

machines = ["Mobile", "Laptop", "Bulb", "Tube Ligt", "Router", "Fan", "Projector", "Air Conditioner"]
print("loop through a list".title())
for x in machines:
    print(x)

print("loop throgh the index numbers".title())

for i in range(len(machines)):
    print(machines[i])

print("loop using the length of the list".title())

m = 0
while m < len(machines):
    print(machines[m])
    m +=1

print("loop using list comprehension. it offers the shortest syntex for looping.".capitalize())
[print(x) for x in machines]
[print(x) for x in machines]
[print(x) for x in machines]
[print(x) for x in machines]