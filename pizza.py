#nested if condition solve
print("Welcome to the pizza delivers.")
size = input("What kind of size Pizza you want? S/M/L ")

bill = 0
if size == "S":
    bill+=15

elif size == "M":
    bill+=20

elif size == "L":
    bill+=25    

else:
    print("Warning!You have typed the wrong input.")


peporoni = input("Do you want to add peporoni?? Y/N ")
if size == "S":
    if peporoni == "Y":
        bill+=2

elif size =="M" or size =="L":
    bill+=3

cheese = input("Do you want extra cheese? Y/N ")
if cheese == "Y":
    bill+=1
else:
    bill+=0

print(f"Your Total bill is ${bill} ")        