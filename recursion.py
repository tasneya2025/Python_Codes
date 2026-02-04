def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

show(4)  


#factorial using recursion 
def calculate_fact(n):
    if(n==1 or n==0):
        return 1
    fact = calculate_fact(n-1)*n
    return fact

fact = calculate_fact(5)
print(fact)


#calculate n number of sum
def calculate_sum(n):
    if(n==0):
        return 0
    return calculate_sum(n-1) + n
    

sum = calculate_sum(5)
print(sum)



#write a recursive function to print all things in a list
def print_list(list,indx):
    if(indx==len(list)):
        return 
    print(list[indx])
    print_list(list,indx+1)

list = ["January","February","March","April"]
print_list(list,0)