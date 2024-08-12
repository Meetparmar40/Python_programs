str = input("Enter your string : ")

a = str[0]
b = str[len(str)-1]

str = b + str[1:len(str)-1] + a

print(str)