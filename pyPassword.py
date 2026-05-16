import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','+']

password_list = []

print("Welcome to password generator!")
user_letter = int(input("How many letters do you want? "))
user_number = int(input("How many numbers do you want? "))
user_symbol = int(input("How many symbol do you want? "))

for char in range(0,user_letter):
    letterPass = random.choice(letters)
    password_list.append(letterPass)

for char in range(0,user_number):
    numberPass = random.choice(numbers)
    password_list.append(numberPass)

for char in range(0,user_symbol):
    symbolPass = random.choice(symbols)
    password_list.append(symbolPass)


random.shuffle(password_list)


password = " "
for char in password_list:
    password += char

print(f"Your automatic generated password is: {password}")










