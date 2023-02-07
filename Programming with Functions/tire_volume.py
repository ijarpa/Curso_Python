# tire volume

from math import pi
from datetime import datetime

date = datetime.now(tz=None)

def tire_volume():
    print('Enter the following data: \n')
    width = float(input('width of the tire in millimeters: '))
    aspect = float(input('aspect ratio of the tire: '))
    diameter = float(input('diameter of the wheel in inches: '))
    volume_numerator = pi * width**2 * aspect * (width * aspect + (2540 * diameter))
    volume = volume_numerator/10000000000

    user_confirmation = input("Do you want to buy tires with the these dimensions (yes/no): ")
    if user_confirmation.lower() == "yes":
        phone = int(input("Please, enter your phone number: "))

        print(f"\nThe approximate volume is: {volume:.2f} liters")

        #with open('volumes.txt', mode="r") as volumes:
            #line_count = len(volumes.readlines())

        with open('volumes.txt', mode="at") as volumes:    
            print(f"{date:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {phone}", file=volumes)

    else:
        print("Thank you")

tire_volume()



