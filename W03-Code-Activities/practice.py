def water_column_height(tower_height, tank_height):
        height = tower_height + 3 * tank_height / 4
        return height

def pressure_gain_from_water_height(height):
        #TODO: Need to implement
        p = 998.2    
        g = 9.80665
        h = height
        return (p*g*h)/1000

wh=water_column_height(5,6)
ph=pressure_gain_from_water_height(wh)

print(f"{wh} ,{round(ph,3)}")