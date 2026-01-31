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


