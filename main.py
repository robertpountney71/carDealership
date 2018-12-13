from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle
'''
The price of a vehicle in the dealership: $5,000 x number of wheels a vehicle has. 
When buying back vehicles offer a flat rate - 10% of the miles driven on the vehicle. 
For trucks, that rate is $10,000. For cars, $8,000. For motorcycles, $4,000.
'''

car = Car(0, 'Honda', 'Accord', 2014, None)
truck = Truck(1000, 'Dodge', 'Charger', 2017, True)
motorcycle = Motorcycle(50000, 'Ducati', 'Hypermotard', 2013, None)
print(car.base_sale_price, car.sale_price(), car.purchase_price(), car.vehicle_type(), car.wheels)
print(truck.base_sale_price, truck.sale_price(), truck.purchase_price(), truck.vehicle_type(), truck.wheels)
print(motorcycle.base_sale_price, motorcycle.sale_price(), motorcycle.purchase_price(), motorcycle.vehicle_type(), motorcycle.wheels)
