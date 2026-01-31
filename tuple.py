#list is mutable ... tuples are immutable 
tup=(1,2,1,3)
print(type(tup))

tup1 =(1,) #for that comma it will treat like a tuple otherwise it will treat like an interger number 
print(type(tup1))

tup2 =(1)
print(type(tup2))


print(tup.index(3))
print(tup.count(1))
