import csv

def main():

    PRODUCT_INDEX = 0

    print("All products")
    products_dic = read_dictionary("products.csv",PRODUCT_INDEX) 

    print(products_dic)

    with open("request.csv","rt") as request_list:

        next (request_list)

        for i in request_list:
            line = i.split(",")
            product_required = line[0]
            quantity = line[1]


            print("Request items:")
            
            



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
