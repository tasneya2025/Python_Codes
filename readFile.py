#HOW TO READ A FILE
f = open("demo.txt","rt")
# data = f.read(5)
# print(data)
# print(type(data))

#after data print we have nothing to read so in line1 it will print an empty next line
line1 = f.readline()
print(line1)
f.close()



