#for triverse we can use for loop

veggies = ["potato","bringle","ladyFinger","Cucumber"]
for vegi in veggies:
    print(vegi)


nums = [1,4,6,3,6,9]
for num in nums:
    print(num) 


tups=(44,98,33,28,70)
for tup  in tups:
    print(tup)     


str = "RephaTasneya"
for char in str:
    print(char)



numbers = (45,67,49,34,78,99,76,49,22,10)
x = 49
indx = 0
for numbs in numbers:
    if(x==numbs):
        print(x," found at index ",indx)
    indx+=1



#range in for loop (by default start from 0)
for i in range(10): #range(stop)
    print(i)  



for i in range(2 , 10): #range(start,stop)
    print(i) 



for i in range(2,10,2): #range(start,stop,step)
    print(i) 



#print backwords numbers from 100 to 1

for i in range(100,0,-1):
    print(i)    


#print multiplication
n = int(input("Enter the number: "))
for i in range(1,11):
    print(n*i)



# if we do not want to execute anything in our loops we use pass . without pass if we leave it empty it will give an error

for i in range(0):
    pass

print("Hi I am Repha")