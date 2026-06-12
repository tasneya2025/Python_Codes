age = int(input("What's your current age: "))
def life_in_weeks(age):
    total_year_left = 90 - age
    total_week_left = total_year_left * 52
    print(f"You have {total_week_left} weeks left.")

life_in_weeks(age) 