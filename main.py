import math as m

RADIUS = 6371.01
is_correct = False

lat1 = m.radians(50.45)
lon1 = m.radians(30.523)

lat2 = m.radians(51.5072)
lon2 = m.radians(-0.1275)
while not is_correct:
    lat1_e = ''
    lat1_e = input("Enter lat for 1'st city:    (default: Kyiv 50.45)\n")
    if lat1_e:
        try:
            lat1 = float(lat1_e)
            is_correct = True
        except ValueError:
            print("not a correct value")
    else:
        is_correct = True

distance = RADIUS*(m.acos(m.sin(lat1)*m.sin(lat2)+m.cos(lat1)*m.cos(lat2)*m.cos(lon1-lon2)))

print(distance)