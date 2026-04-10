import csv
from datetime import datetime,date


def main():

    PRODUCT_INDEX = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2
    


    print("All products")
    try:
        products_dic = read_dictionary("products.csv",PRODUCT_INDEX)
    
    except FileNotFoundError:
        print("File not found, review the name or if the file exist.")


    print(products_dic)
    print("")

    

    with open("request.csv","rt") as request_list:

        next (request_list)

        subtotal = 0
        number_of_items = 0

        print("Inko Emporium")
        print(" ")

        for i in request_list:
            line = i.split(",")
            product_required = line[0]
            quantity = int(line[1])
            product_request = products_dic[product_required]
            price = float(product_request[PRODUCT_PRICE])
            subtotal += price * quantity
            number_of_items += quantity
            
            print(f"{product_request[PRODUCT_NAME]}: {quantity} @ {product_request[PRODUCT_PRICE]}")
        
        sales_tax = round(subtotal * 0.06,2)
        total = subtotal + sales_tax
        today = datetime.now()

        print(f"Number of items: {number_of_items}")
        print(f"Subtotal: ${round(subtotal,2)}")
        print(f"Sales tax: {sales_tax}")
        print(f"Total: {total}")
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{today.strftime("%a %b %d %H:%M:%S %Y")}")

    pass

def read_dictionary(filename,key_value):

    #Set a dictionary by first
    dictionary = {}

    #Open the external file to creat the compund dictionary
    with open(filename,"rt") as csv_file:

        reader = csv.reader(csv_file)
        #This skip the first line in the csv document
        next(reader)
        #With the following loop we can append the values in the dictionary
        for row_list in reader:
            key = row_list[key_value]
            dictionary[key] = row_list


    return dictionary

if __name__ == "__main__":
    main()
