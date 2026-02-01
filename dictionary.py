info = {
    "key" :"value",
    "name" : "Urbi",
    "age" : 23,
    "is_adult" : True,
    "subjects" : ["python","C++","java"],
    "topic" : ("dictionary",)


}

print(info)
print(type(info))


print(info["name"])
print(info["is_adult"])

#dictionary is mutable
info["hobby"] = "drawing"
print(info)

info["name"] = "Tasneya"
print(info)



null_dict ={

}

print(null_dict)

#nested dictionary

student = {
    "name" :"Repha Tasneya",
    "subjects" : {
        "phy" :98,
        "chem" : 99,
        "biology" :100
                 
    }

}

print(student["subjects"]["chem"])

#dictionary methods 
print(student.keys()) #not return nested keys
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))


print(student.items())#tuples return with key and value
pairs = list(student.items())
print(pairs[0])


#get and key method can give values but after get method the code will still execute (none) if eror present, which will not in key it will give an error

print("Before")
# print(student["name2"])
print(student.get("name2"))
print("after")


student.update({"city" : "Dhaka"})
print(student)

new_dict = {
    "blood" : "O+",
    "age" :23,
    "name" : "Urbi"
}
student.update(new_dict)
print(student)

