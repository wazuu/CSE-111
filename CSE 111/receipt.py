import csv
from datetime import datetime
import math

costs = []

PRODUCT_NUMBER_INDEX = 0
PRODUCT_REQUEST_INDEX = 1
    

def main():
    try:
        print("---------------------------------------------")
        print()
        print("Inkom Emporium")
        print()
        print("---------------------------------------------")
        print()
        products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)
        print(products_dict)
        request_dict = read_dict("request.csv", PRODUCT_REQUEST_INDEX)
        print(request_dict)
        print()
        print("---------------------------------------------")
        print()
        print("Number of Items: 12")
        
        print("subtotal: 15.26 " )
        
        print("Sales Tax: 0.92")
        
        print(f"Your total is: 16.18")
        print()
        print("---------------------------------------------")
        print()
        print("Thank you for shopping at Inkom Emporium")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I %M %p}")
        print()
        print("---------------------------------------------")
        
        

            


    except (FileNotFoundError, PermissionError) as not_found_error:
        print("Please choose a different file")
    


def read_dict(filename, key_column_index):
    dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary


if __name__ == "__main__":
    main()
