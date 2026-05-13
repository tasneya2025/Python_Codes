import random

#random integar
random_integar = random.randint(1,10)
print(random_integar)

#random number 0 to 1
random_numb = random.random()
print(random_numb)

#random float number
random_float = random.uniform(1,10)
print(random_float)


#Heads vs Tail game
game = random.randint(0,1)
if game == 0:
    print("Heads")
else:
    print("Tails")    



#who gonna pay bill ???
friends = ["Alice","Bobby","Jack","Daniel"]

print(random.choice(friends)) #solution number 1

ran_index = random.randint(0,3)#solution number 2
print(friends[ran_index])
