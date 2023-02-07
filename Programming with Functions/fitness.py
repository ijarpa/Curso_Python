"""
Health professionals who are helping a client achieve a healthy body weight, 
sometimes use two computed measures named body mass index and basal metabolic rate.
"""

from datetime import datetime

def main():
    gender = input("Please enter your gender (women/men): ").lower()
    birthday = input("Enter yout birthdate in this format YYYY-MM-DD: ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))

    bmi = bmi_index(pounds, inches)
    bmr = bmr_rate(gender, pounds, inches, birthday)

    print(compute_age(birthday))
    print(kg_from_lb(pounds))
    print(cm_from_in(inches))
    print(f"{bmi:.2f}")
    print(f"{bmr:.2f}")

    
def compute_age(birthday):
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthday.year

    if birthday.month > today.month or (birthday.month == today.month and birthday.day > today.day):
        age -= 1

    return age

def kg_from_lb(pounds):
    weight_kg = pounds * 0.45359237
    return weight_kg

def cm_from_in(inches):
    height_cm = inches * 2.54
    return height_cm

def bmi_index(pounds, inches):
    weight_kg = kg_from_lb(pounds)
    height_cm = cm_from_in(inches)
    bmi = (10000 * weight_kg) / height_cm*height_cm
    return bmi

def bmr_rate(gender, pounds, inches, birthday):
    weight_kg = kg_from_lb(pounds)
    height_cm = cm_from_in(inches)
    age = compute_age(birthday)    

    if gender == "women":
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)

    return bmr

main()

