#program to find the greatest of three numbers
#num1
#num2
#num3
#greatest

#input block
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))


#if block

if(num1 > num2):
    if(num1 > num3):
        greatest = num1
    else:
        greatest = num3
elif(num2 > num3):
    greatest = num2
else:
    greatest = num3

print(greatest)