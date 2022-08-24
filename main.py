import math as m

def check_input(default_value, text):
    is_correct = False
    input_value = ''
    while not is_correct:
        input_value = input(text)
        if input_value:
            try:
                output_value = float(input_value)
                is_correct = True
            except ValueError:
                print("not a correct value")
                is_correct = False
        else:
            is_correct = True
            output_value = default_value
    return output_value

#default values
RADIUS = 6371.01
lat1 = 50.45
lon1 = 30.523
lat2 = 51.5072
lon2 = -0.1275
#---

lat1 = m.radians(check_input(lat1, "Enter lat for the 1'st city:    (default: Kyiv 50.45)\n"))
lon1 = m.radians(check_input(lon1, "Enter lon for the 1'st city:    (default: Kyiv 30.523)\n"))
lat2 = m.radians(check_input(lat2, "Enter lat for the 2'nd city:    (default: London 51.5072)\n"))
lon2 = m.radians(check_input(lon2, "Enter lon for the 2'nd city:    (default: London -0.1275)\n"))



distance = RADIUS*(m.acos(m.sin(lat1)*m.sin(lat2)+m.cos(lat1)*m.cos(lat2)*m.cos(lon1-lon2)))

print(distance)