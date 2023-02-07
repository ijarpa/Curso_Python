import numbers
from random import uniform

def main():
    numbers = [16.2, 75.1, 52.3]
    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 2)
    print(numbers)

def append_random_numbers(number_list, quantity=1):
    for i in range(quantity):
        random_number = round(uniform(0, 100), 1)
        number_list.append(random_number)

if __name__ == "__main__":
    main()




