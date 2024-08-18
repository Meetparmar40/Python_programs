marks = []

for i in range(1, 4):
    marks.append(int(input("Enter the matks of test")))

marks.sort()

print("The best of average of two tests is", (marks[1] + marks[2])/2)