import Computations as comp
y = comp.Computations(10,10000000,10,10)

print ("Antenna Length")
print (y.calcAntennaLength())
print (" ")
print ("Latency")
print (y.calcLatency())
print (" ")
print ("nonstationary Diameter")
print (y.calcDishDiameter())
print (" ")
print ("stationary Diameter")
print (y.calcGeoStationaryDishDiameter())
print (" ")