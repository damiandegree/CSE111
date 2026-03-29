from formula import parse_formula

def make_periodic_table():
    with open ("periodic_table.txt","r",encoding="utf-8") as f:

        periodic_table_dict = {}

        for i in f:
            line = i.split(",")
            symbol = line[0]
            name = line[1]
            mass = float(line[2])

            periodic_table_dict[symbol] = [name,mass] 
    return periodic_table_dict 


def compute_molar_mass(symbol_quantity_list, periodict_table_dict):

    total_mass = 0

    for i in symbol_quantity_list:
        element = i
        symbol = element[0]
        quantity = int(element[1])

        if symbol in periodict_table_dict:
            
            value = periodict_table_dict[symbol]
            mass = value[1]
            atomic_mass = mass * quantity
    
        total_mass += atomic_mass

    return total_mass

def main():

        chemical_formula = input("Introduce a chemical formula: ")

        sample_size = float(input("Introduce de sample mass in grams: "))

        periodic_table = make_periodic_table()

        elements_list = parse_formula(chemical_formula,periodic_table)

        total_mass = compute_molar_mass(elements_list,periodic_table)

        print(f"The molar mas is {total_mass} grams/mole")

        number_of_moles = sample_size/total_mass

        print(f"The number of moles is {number_of_moles:.5f} moles. ")

    # 1 Asks the user for a chemical formula.
    # 2 Asks the user for the sample size in grams.
    # 3 Call make_periodic_table function and store returned dictionary in variable.
    # 4 Call parse_formula (from provided library) to get a list of elements in formula. 
    # (store in a variable).
    # 5 Call compute_molar_mass to calculate the molar mass. 
    # Pass in the periodic table dictionary and element list returned from the previous functions.
    # 6 Display the molar mass.
    # 7 Calculate Number of moles in the sample.
    

if __name__ == "__main__":
    main()





