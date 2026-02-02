#set is mutable but elements are immutable so we cannot pass list and dictionary there ...repeated values only print once 
collection ={1,2,2,"hello","world","world",2,1,4}
print(collection)
print(type(collection))

collcetion2 = set() #for an empty set if we write collection 2 = {} ...its type will be dictionary 
print(type(collcetion2))




#methods of set
collcetion2.add(1)
collcetion2.add("Urbi")
collcetion2.add(1)
collcetion2.add(2)
# collection.add([1,2,3]) #unhashable type error will come
collcetion2.remove(1)
# collcetion2.clear()
print(collcetion2)

print(collcetion2.pop())#it removes random value/values from sets



set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
