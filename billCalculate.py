print("Hey welcome to the XYZ center!")
bill= float(input("What is your total bill? "))
tip = int(input("how many percent tip you wanna give? $ (5/10/12/15) "))
num_of_people = int(input("How many people you wanna split the bill? "))

bill_after_tip = bill*(tip/100)+bill
final_bill = bill_after_tip/num_of_people
print(f"Each of you will pay: ${final_bill}")