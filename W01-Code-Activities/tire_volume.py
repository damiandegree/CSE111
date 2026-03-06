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

    print("Please enter the measures of your tire.")
    
    width = float(input("Enter the width of yout tire in mm: "))
    ratio = float(input("Enter the aspect ratio: "))
    diameter = float(input("Enter the diamenter of the wheel in inches: "))
    volume = round((math.pi * width**2 * ratio * (width * ratio + 2540 * diameter))/10000000000,2)
    print(f"The volume of your tire is: {volume} liters.")
    
    print(f"{width}/{ratio:}R{diameter}, V = {volume}L",file = volumes)
        