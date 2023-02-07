# discount

from datetime import datetime

current_day = datetime.now()
day_week = current_day.weekday()

programm = 1

while programm != 0:
    
    subtotal = float(input("customer's subtotal: "))

    if subtotal >= 50 and day_week == 1 or day_week == 2:
        discount = subtotal * 0.1
        tax = (subtotal - discount) * 0.06
        total = subtotal - discount + tax
        print(total)

    elif subtotal < 50 and day_week == 1 or day_week == 2:
        difference = 50 - subtotal
        print(difference)

    else:
        tax = subtotal * 0.06
        print(subtotal + tax)

    programm = int(input("do you want to repeat the process yes(1) / no(0) : "))

