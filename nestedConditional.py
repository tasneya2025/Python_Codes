# age = int(input("Enter your age: "))

# if(age>=18):
#     if(age>88):
#         print("You are way to old for driving")
#     else:
#         print("You are eligible for driving")
# else:
#     if(age<0):
#         print("Please enter an appropriate age!!")
#     else:
#         print("You are not eligible for driving")            

print("Hello Welcome to the Fantasy Kingdom Park!!")
height = float(input("Enter your height: "))
if height >= 120:
    print("You can ride the rollar coster.")
    age= int(input("Enter your age: "))
    if age>18:
        print("You have to pay $10.")

    elif age==18:
        print("The ride is free for you") 

    else:
        print("you have to pay $5.")
else:
    print("SORRY,You are not fit for this rollar coster ride!!")            