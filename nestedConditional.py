age = int(input("Enter your age: "))

if(age>=18):
    if(age>88):
        print("You are way to old for driving")
    else:
        print("You are eligible for driving")
else:
    if(age<0):
        print("Please enter an appropriate age!!")
    else:
        print("You are not eligible for driving")            