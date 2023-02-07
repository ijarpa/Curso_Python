import csv
from datetime import datetime

date = datetime.now()

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    try:
        with open(filename, "rt") as csv_file:

            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list
        
        return dictionary

    except FileNotFoundError as error:
        print(error)
        print("Please choose a different file")

def subtotal(list_quantity, list_subtotal):

    weekday = f"{datetime.today():%A}"
    quantity_suma = sum(list_quantity)  
    subtotal_suma = sum(list_subtotal)

    print("")

    if weekday == "Tuesday" or weekday == "Wednesday":
        subtotal_suma = subtotal_suma * 0.9 
        subtotal = subtotal_suma * 0.06
        print(f"Number of Items: {quantity_suma:.0f}")
        print(f"Subtotal: {subtotal_suma:.2f}")
        print(f"Sales Tax: {subtotal:.2f}")
        print(f"Total: {(subtotal + subtotal_suma):.2f}")

        print("\nThank you for shopping at the Inkom Emporium.")
        print(f"{date:%A %b %I:%M %p}")
    else:
        subtotal = subtotal_suma * 0.06
        print(f"Number of Items: {quantity_suma:.0f}")
        print(f"Subtotal: {subtotal_suma:.2f}")
        print(f"Sales Tax: {subtotal:.2f}")
        print(f"Total: {(subtotal + subtotal_suma):.2f}")

        print("\nThank you for shopping at the Inkom Emporium.")
        print(f"{date:%A %b %I:%M %p}")




def main():

    product_index = 0
    filename = 'products.csv'

    product_dict = read_dictionary(filename, product_index)
    #print("All Products")
    #for i, values in product_dict.items():
    #    print(i, values)


    try:
        quantity_list = []
        subtotal_list = []

        with open('request.csv', "rt") as csv_file:

            request_list = csv.reader(csv_file)
            next(request_list)

            print("\nInkom Emporium\n")
            for item in request_list:
                product_id = item[0]
                quantity = float(item[1])

                product_item = product_dict[product_id]
                product_name = product_item[1]
                product_price = float(product_item[2])

                print(product_name, quantity, product_price)

                quantity_list.append(quantity)
                subtotal_list.append(product_price * quantity)

        

    except KeyError as keyerror:
        print(f"Product {keyerror} not found.")

    subtotal(quantity_list, (subtotal_list))


if __name__ == "__main__":
    main()