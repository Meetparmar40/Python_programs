str = input("Enter the string ")
digit = 0
up = 0
lw = 0
words = 0
for i in str:
    if i.isupper():
        up += 1
    if i.islower():
        lw += 1
    if i == ' ':
        words += 1
    if i.isnumeric():
        digit += 1

words += 1
print("Number of digits = ", digit)
print("Number of lowercase letters = ", lw)
print("Number of uppercase letters = ", up)
print("Number of words = ", words)