#WAP to find the sum of first n numbers

n = 10 #using for loop
sum =0
for i in range(1,n+1):
    sum+=i
    i+=1
print(n," numbers of sum is ",sum)    

#using while loop
sum2=0
indx=1
while indx<=n:
    sum2+=indx
    indx+=1

print("total sum is ",sum2)  


#WAP to find the factorial of first n number

n = 5 #using for loop
fact = 1
for i in range(1,n+1):
    fact*=i
    i+=1
print(n," numbers of factorial is ",fact)     

#using while loop
fact2=1
indx=1
while indx<=n:
    fact2*=indx
    indx+=1

print("total factorial is ",fact2)