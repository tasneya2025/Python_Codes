def calculate_love_score(name1,name2):
    list1 = (name1+name2).upper()
    count =0
    for word in list1:
        if(word=="T"):
            count+=1
        elif(word=="R"):
            count+=1
        elif(word=="U"):
            count+=1
        elif(word=="E"):
            count+=1

    love_count = 0       
    for word in list1:
        if(word=="L"):
            love_count+=1
        elif(word=="O"):
            love_count+=1
        elif(word=="V"):
            love_count+=1
        elif(word=="E"):
            love_count+=1
    total = count*10+love_count
    print(total)

    

calculate_love_score("Kanye West","Kim Kardashian")    