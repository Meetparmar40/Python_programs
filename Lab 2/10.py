num = input("Enter the number ")

reverse = num[::-1]

if(num == reverse):
    print("Is Palindrome")
else:
    print("Is not Palindrome")

count = {}

for i in num:
    count[i] = 0
for i in num:
    count[i] += 1

for i in count:
    print(i, "appears", count[i], "times")
