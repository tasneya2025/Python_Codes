#HOW TO WRITE A FILE
#there are 2 types of write : write(w)-->overwrite and append(a)-->at the end add 
f = open("demowrite.txt","w")
f.write("I want to learn python")
f.close()

f = open("demowrite.txt","a")
f.write("\nThen I will learn panda,tensorflow In sha Allah")
f.close()

#if there will no file to write or append python will create a new file 
f=open("sample.txt","w")
f.close()

f=open("sample.txt","a")
f.close()

#if we want to overwrite on starting we will use r+
f = open("demowrite.txt","a+")

print(f.read())
f.write("abc")
f.close

#r+ read + overwrite (pointer -->start)-->no truncate
#w+ read + overwrite --> truncate
#a+ read + append     (pointer -->end)-->no truncate




