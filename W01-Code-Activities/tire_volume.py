#Have the user enter a tire width in mm.
#Have the user enter the aspect ratio.
#Have the user enter the diameter of the wheel in inches.
#Calculate and display the tire's volume.
#Log the information in a text file.
#current date (Do NOT include time)
# width of the tire
#aspect ratio of the tire
#diameter of the wheel
#volume of the tire (rounded to two decimal places}
import math
from datetime import datetime

with open("volume.txt","at") as volumes:
    print("")
    print("Enter the measures of your tire:")
    while True:
            try:
                width = int(input("Enter the width of your tire in mm: "))
            except ValueError:
                 print("Introduce a valid number.")
                 continue
            try:
                ratio = int(input("Enter the aspect ratio: "))
            except ValueError:
                 print("Introduce a valid number.")
                 continue
            try:
                diameter = int(input("Enter the diamenter of the wheel in inches: "))
            except ValueError:
                 print("Introduce a valid number.")
                 continue
            
            volume = round((math.pi * width**2 * ratio * (width * ratio + 2540 * diameter))/10000000000,2)
            print(f"The volume of your tire is: {volume} liters.") 

            print(f"{width}/{ratio}R{diameter}, V = {volume}L",end="\n",file = volumes, flush=False)
            option = input("Continue?: YES/NO: ").lower()

            if option == "no":
                break
            elif option == "yes":
                 continue
            else:
                print("Type a correct answer.")
        