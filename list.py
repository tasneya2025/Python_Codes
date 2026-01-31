student =["karan",10.5,30]
print(student)
student[0]="arjun"
print(student)
print(len(student))

#list slicing 
marks =[20,30,40,50]
print(marks[1:3])
print(marks[:3])
print(marks[1:])
print(marks[-3:-1])


#list methods 
roll = [20,89,45,11,75,66]
roll.append(45)
print(roll)

roll.sort()
print(roll)

# roll.reverse()
# print(roll)

roll.insert(2,33)
print(roll)

roll.remove(89)
print(roll)

roll.pop(6)
print(roll)


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist1 = ["apple", "banana", "cherry"]
thislist1.clear()
print(thislist1)