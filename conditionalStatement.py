a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if(a>b and a>c and a>d):
    print("a is the largest",a)

elif(b>c and b>d):
    print("b is the largest",b)

elif(c>d):
    print("c is the largest",c)

else:
    print("d is the largest",d)   

    #if the if condition is false then it will check elif otherwise it wont 