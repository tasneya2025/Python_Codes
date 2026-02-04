#WAP to print the list in a single line using function
heroes = ["Thor","Spiderman","Doctor Strange","Loki"]

def print_fuction(list):
    for person in list:
        print(person,end=" ")


print_fuction(heroes)
print()


#WAP to calculate factorial using function
def fact_calculate(n):
   fact = 1 
   for i in range(1,n+1):
      fact*=i
      
   print(fact)
   
fact_calculate(5)


#WAP to convert USD to BDT using function
def calculate(USD):
    BDT = USD*130
    print(USD," USD = ",BDT," Taka")

calculate(34)  


