str1 = input("Enter the string 1 ")
str2 = input("Enter the string 2 ")

a = str1[0]
b = str2[0]

str = b + str1[1:len(str1)] + " " + a + str2[1:len(str2)]

print("The required string is", str)



