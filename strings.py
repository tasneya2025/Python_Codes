name = "Repha Tasneya Urbi"
#length of a string
print(len(name))
print("Urbi" in name)


a = " this iS a pen "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("i","e"))
print(a.split("i"))

#format strings
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#slicing of a string
print(name[0:5])
print(name[5:])
print(name[-4:-1])
print(name[-4:])


#string function 
str = "i am a am coder."
print(str.endswith("er."))  #returns true if string ends with substr 
print(str.capitalize())  #capitalizes 1st char 
print(str.replace("am","is"))  #replaces all occurrences of old with new 
print(str.find("a"))  #returns 1st index of 1st occurrence 
print(str.count("am")) 

#isDigit
txt = "a50800"
x = txt.isdigit()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())



