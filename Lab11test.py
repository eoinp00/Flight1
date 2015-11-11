from Lab11Aircraft import *
from Lab11Tower import *

myTower = Tower("Dublin", ["Ei101", "EI102", "EI102", "ooooooo", "EI09898"])
#myTower.aFlightList["Ei101", "EI102", "EI102"]
print ("aFlightlist is: ") #myTower.aFlightList)
myTower.validateFlightNum()

myjumbo= Aircraft("747")
myjumbo.setFlightNumber("EI101")
print("About to start preparing a ", myjumbo.planeType, " for takeoff")

myjumbo.addFuel(30)
myjumbo.printStatus()
myjumbo.fuelCheck()
myjumbo.takeOff()

print("---")

myairbus= Aircraft("A380")
print("About to start preparing a ", myairbus.planeType, " for takeoff")
myairbus.addFuel(2000)
myairbus.printStatus()
myairbus.fuelCheck()
myairbus.takeOff()

print("---")

myBoeing= Aircraft("737")
print("About to start preparing a ", myBoeing.planeType, " for takeoff")
fuelInTruck = 50000
fuelInTruck = myBoeing.addFuel(fuelInTruck)
myBoeing.printStatus()
myBoeing.fuelCheck()
myBoeing.takeOff()
print("Fuel Truck still has:", fuelInTruck)







