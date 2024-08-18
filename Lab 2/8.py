sides = []

for i in range(1, 4):
    sides.append(int(input("Enter the side ")))

sides.sort()

if sides[0]**2  + sides[1]**2 == (sides[2] * sides[2]):
    print("Given Triangle is right angle triangle")
else:
    print("Given Triangle is not a right angle triangle")