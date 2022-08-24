from dis import dis
import math as m

RADIUS = 6371.01

lat1 = m.radians(50.45)
lon1 = m.radians(30.523)

lat2 = m.radians(51.5072)
lon2 = m.radians(-0.1275)

distance = RADIUS*(m.acos(m.sin(lat1)*m.sin(lat2)+m.cos(lat1)*m.cos(lat2)*m.cos(lon1-lon2)))

print(distance)