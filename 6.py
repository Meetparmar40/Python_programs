str1 = input("Enter the string : ")

i, j = 0, len(str1) - 1
check = True
while i < j:
    if str1[i] == str1[j]:
        i+=1
        j-=1
    else:
        check = False
        break

if check:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
