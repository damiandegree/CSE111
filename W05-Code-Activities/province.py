with open("provinces.txt","rt") as file:

    row_list = []
    
    for i in file:
        line = i.strip()
        if line == "AB":
            line = "Alberta"
        row_list.append(line)

row_list.pop(0)
row_list.pop(-1)

print(row_list,end="\n")
print("The times the name Alberta appears in the list is ", row_list.count("Alberta"))