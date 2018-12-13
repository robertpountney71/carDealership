from Vehicle import Vehicle

class Truck(Vehicle):

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return the type of vehicle this is."""
        return 'truck'