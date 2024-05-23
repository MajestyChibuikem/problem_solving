"""finding the cgpa
first_name:first name of the user
last_name: last name of the user
cgpa:the cgpa of the user
gp:the string cgpa of the user
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")


cgpa = float(input("Enter your CGPA: "))

#if block
if cgpa > 4.5 and cgpa <= 5.0:
    gp = "First class"
elif cgpa > 3.5 and cgpa <= 4.5:
    gp = "Second class Upper"
elif cgpa > 3.0 and cgpa <= 3.5:
    gp = "Second class lower"
elif cgpa > 2.0 and cgpa <= 3.0:
    gp = "Third class"
elif cgpa > 0.0 and cgpa <= 2.0:
    gp = "Pass"
else:
    print("Error!")


print(first_name, last_name,"CGPA is",gp)