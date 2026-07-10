# calculates employee bonus based on performance rating

def calculate_bonus(salary, rating):
    if rating >= 4.5:
        percent = 20
    elif rating >= 4:
        percent = 15
    elif rating >= 3:
        percent = 10
    else:
        percent = 0
    return salary * percent / 100



salary = float(input("Enter salary: "))
rating = float(input("Enter performance rating: "))
print(f"Bonus: {calculate_bonus(salary, rating)}")
