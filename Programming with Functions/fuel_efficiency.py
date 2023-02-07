# function fuel efficiency


def main():
    start = int(input("Starting odometer value in miles: "))
    end = int(input("ending odometer value in miles: "))
    fuel = float(input("Amount of fuel in gallons: "))

    mpg = miles_per_gallon(start, end, fuel)

    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f}")
    print(f"{lp100k:.2f}")

def miles_per_gallon(start, end, fuel):
    mpg = abs(end - start) / fuel
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k


main()

