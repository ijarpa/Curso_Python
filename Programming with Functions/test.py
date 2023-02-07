from datetime import datetime

date = datetime.now()

weekday = f"{datetime.today():%A}"



def subtotal(list_quantity, list_subtotal):

    quantity_suma = sum(list_quantity)  
    subtotal_suma = sum(list_subtotal)

    print("")
    subtotal = subtotal_suma * 0.06
    print(f"Number of Items: {quantity_suma:.0f}")
    print(f"Subtotal: {subtotal_suma:.2f}")
    print(f"Sales Tax: {subtotal:.2f}")
    print(f"Total: {(subtotal + subtotal_suma):.2f}")

    print("\nThank you for shopping at the Inkom Emporium.")
    print(f"{date:%A %b %I:%M %p}")



quantity_list = [2,42,4]
subtotal_list = float[10,5,20]

discount = 0.9

if weekday == "Tuesday" or weekday == "Wednesday":
    subtotal(quantity_list, (subtotal_list*discount))
else:
    print(0)
